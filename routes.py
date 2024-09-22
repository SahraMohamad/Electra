import os
from flask import Flask, jsonify, request
from flask_cors import CORS

# 
from Network import Network
import handle_data
#

income_data, vote_data, acs_data = handle_data.load_and_handle_data()


def create_app(config=None):    
    app = Flask(__name__)

    app.config.update(dict(DEBUG=True))
    app.config.update(config or {})

    CORS(app)

    # # # # # # # #

    #   ROUTES    #
    
    # # # # # # # #
    @app.route("/")
    def hello_world():
        return "Hello World"

    @app.route("/gen_sim_network", methods=['POST'])
    def gen_sim_network():
        '''
        Generates 
        '''
        form_data = request.form
        state_name = form_data.get('state_name')
        user_scenario = form_data.get('user_scenario')
        num_agents = form_data.get('num_agents', 5)
        
        if not user_scenario or not state_name:
            return jsonify({'error': 'Must provide a user_prompt and state'}), 400
        
        income_result = income_data[income_data['State_Name'].str.lower() == state_name.lower()]
        vote_result = vote_data[vote_data['state'].str.lower() == state_name.lower()]
        acs_result = acs_data[acs_data['State'].str.lower() == state_name.lower()]

        state_data = {
            "income_data": income_result.to_dict(orient='records'),
            "2020_election_vote_data": vote_result.to_dict(orient='records'),
            "acs_data": acs_result.to_dict(orient='records')
        }
        
        agent_network = Network(user_scenario, state_name, num_agents, state_data)
        pre, post, chat = agent_network.simulate('round_robin', 1)
        # result = agent_network.group_chat("round_robin", 1)
        return jsonify({
            'chat': chat,
            'votes': {
                'pre_result': pre, 
                'post_result': post
            }
            }), 200

    @app.route("/get_state_data", methods=['POST'])
    def get_state_data():
        state_name = request.form.get('state_name', '')
        if state_name == '': 
            return jsonify({'Must provide a state_name'}), 400
                
        income_result = income_data[income_data['State_Name'].str.lower() == state_name.lower()]
        vote_result = vote_data[vote_data['state'].str.lower() == state_name.lower()]
        acs_result = acs_data[acs_data['State'].str.lower() == state_name.lower()]
        
        if income_result.empty and vote_result.empty and acs_result.empty:
            return jsonify({"error": f"No data found for state '{state_name}'"}), 404

        income_json = income_result.to_dict(orient='records')
        vote_json = vote_result.to_dict(orient='records')
        acs_json = acs_result.to_dict(orient='records')

        # Combine all results into one dictionary
        result = {
            "income_data": income_json,
            "vote_data": vote_json,
            "acs_data": acs_json
        }

        return jsonify(result), 200

    return app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app = create_app()
    app.run(host="0.0.0.0", port=port)
