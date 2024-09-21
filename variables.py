identities = [
    '''Board Chair: Mark Carney. Mark Carney is the Chair of Brookfield Asset Management and Head of Transition Investing. In this role, he is focused on the development of products for investors that will combine positive social and environmental outcomes with strong risk-adjusted returns.
Mark is an economist and banker who served as the Governor of the Bank of England from 2013 to 2020, and prior to that as Governor of the Bank of Canada from 2008 until 2013. He is currently the United Nations Special Envoy for Climate Action and Finance and Co-Chair for the Glasgow Finance Alliance for Net Zero.
Among other roles, he is also an external member of the Board of Stripe, a member of the Global Advisory Board of PIMCO, a member of Harvard University’s Board of Overseers, and serves on the Bloomberg Philanthropies Board.''',
    '''Patricia E. Harris. Patti is the Chief Executive Officer of Bloomberg Philanthropies and serves on the Management Committee of Bloomberg LP. Previously, she served as the First Deputy Mayor of the City of New York.
Before joining the Bloomberg administration in 2002, she managed Bloomberg LP’s Corporate Communications Department, overseeing its Philanthropy, Public Relations, and Governmental Affairs divisions. She began her career in public service by working for Mayor Ed Koch in New York, where she later became Executive Director of the City’s Art Commission.
She also serves on the boards of the Perelman Performing Arts Center, the Public Art Fund, Franklin & Marshall College, and the National 9/11 Memorial and Museum. She previously served as a trustee of Cornell University.''',
    '''Reed Hastings. Reed Hastings Jr. is the co-founder and Executive Chairman of Netflix, which went public in 2002. He co-founded Netflix in 1997 after he sold his first company, Pure Software, to Rational Software. He stepped down as co-CEO of Netflix in January 2023.
Reed is an active educational philanthropist and served on the California State Board of Education from 2000 to 2004. He is currently on the board of several educational organizations, including KIPP, Pahara, and the Charter School Growth Fund.''',
    '''Annie Lamont. Annie Lamont co-founded Oak HC/FT in 2014 to invest exclusively in healthcare and fintech entrepreneurs. In 2023, Oak HC/FT was named as one of the ten best performing growth equity firms in the world. Annie is also the First Lady of Connecticut.
Prior to founding Oak HC/FT, Annie spent 28 years at Oak Investment Partners, where she served as Managing Partner and led the healthcare and fintech practices.
Annie served as a core participant of the Health and Human Services Deputy Secretary’s Innovation and Investment Summit (DSIIS), a collaboration between HHS and healthcare innovation and investment professionals to discuss the healthcare landscape, emerging opportunities, and the government’s role in facilitating accelerated innovation and investment.
Annie currently serves on boards, including Advise Health Holdings, Brightline, CareBridge, Main Street Health, Modern Age, Quartet, Rubicon Founders, Truepill, Vesta Health and VillageMD. She is a Board Observer at Precision Medicine Group. Annie served on the Board of Trustees at Stanford University.''',
    '''Charles Phillips. Charles Phillips is a Co-Founder and managing partner of Recognize, a technology investment firm focused on software engineering services. Previously, he was the Chairman and CEO of enterprise applications company Infor and President of Oracle Corporation. He served as a Captain in the U.S. Marine Corps and graduated from the Air Force Academy.
Charles is a member of the Defense Innovation Board. He co-founded and serves as Co-Chairman of the Black Economic Alliance, a group of business leaders committed to economic growth in Black communities. He is chairman of the Apollo Theater. He also serves on the board of directors of Paramount, American Express, Compass Inc., and the Council of Foreign Relations.''',
    '''Patti Roskill. Patti Roskill is the Chief Financial Officer of Bloomberg LP and serves on the Management Committee of the company. She was previously a partner at Geller & Company.
She has over thirty years of experience in corporate finance, including accounting, financial planning, analytics and reporting, treasury, compensation, and tax services. After leaving Drexel Burnham Lambert in 1988, Patti joined Geller & Company and began working on raising capital, establishing annual operating and capital budgets and management reporting.
Patti is an active member of USC’s Marshall School of Business’ Board of Councilors.''',
    '''Tom Secunda. Tom Secunda is a co-founder of Bloomberg LP, where he has served in a leadership role for over 40 years. Tom currently serves on the Management Committee of the company. Tom has played an instrumental role in building the Bloomberg Terminal and leading the company’s entry into the enterprise market. Before helping found Bloomberg, Tom was a fixed-income trader at Morgan Stanley and was in systems research at Salomon Brothers.
Tom serves as chairman of the Jamaica Bay-Rockaway Parks Conservancy, Trustee Emeritus of the National Parks Conservation Association, and is on the board of the Manhattan Theatre Club, where he serves as the President and Chair of the Executive Committee. He is on the board of the Intrepid Museum Foundation, the Simon Wiesenthal Center, and is Chairman of the board of Love City Strong, Inc. Tom also serves on the Jacobs Technion-Cornell Institute Advisory Council.''',
    '''Robert K. Steel. Bob Steel is a Partner and Vice Chairman at Perella Weinberg Partners. He joined the firm in 2014 and served as CEO from 2014-2019.
Prior to joining Perella Weinberg Partners, Bob was Deputy Mayor for Economic Development during the Bloomberg administration; President and CEO of Wachovia Corporation, overseeing the sale of the bank to Wells Fargo & Co.; and Under Secretary for Domestic Finance at the U.S. Department of Treasury. He previously spent nearly 30 years at Goldman Sachs, rising to head of the Global Equities Division, Vice Chairman of the firm, and a member of its Management Committee.
Among his many board roles, he serves on the executive committee of the Partnership for New York City, the board of directors of the Lincoln Center for the Performing Arts, Rockefeller University, The Morgan Library and as a trustee and former chairman of the Aspen Institute Board of Trustees.''',
    '''Joshua L. Steiner. Josh Steiner is a partner at SSW, a private investment firm, and a senior adviser at Bloomberg LP, where he previously was head of industry verticals. He also previously served as chairman of the Board of Directors at Castleton Commodities International LLC.
Prior to joining Bloomberg, Josh co-founded and was co-president of Quadrangle Group, LLC, a private equity and asset management firm. Before co-founding Quadrangle, he was a managing director at Lazard Frères & Co. LLC. From 1993 to 1995 he served as chief of staff for the U.S. Department of the Treasury.
He currently serves on the board of Yale University, the International Rescue Committee and the SNF Agora Institute at Johns Hopkins University.''',
    '''Darren Walker. Darren Walker is president of the Ford Foundation. Prior to joining Ford, he was vice president at the Rockefeller Foundation, and in the 1990s, he served as COO of the Abyssinian Development Corporation, Harlem’s largest community development organization. He had a decade long career in international law and finance at Cleary Gottlieb Steen & Hamilton and UBS.
He serves on the boards of PepsiCo and the Ralph Lauren Corporation. In addition, he serves on the boards of several nonprofits, including the National Gallery of Art, Lincoln Center for the Performing Arts, the Clooney Foundation for Justice, and the Committee to Protect Journalists.''']

backstory_message = [
                {
                    "role": "system",
                    "content": '''Develop a deeply realistic, human-like backstory that equally explores both 
                    the strengths and flaws of the character. Include raw, gritty details that reflect 
                    the complexity of real life — highlighting their habits, desires, personality traits, and quirks, 
                    while also diving into their struggles, insecurities, and imperfections. Focus on 
                    the challenges they've faced, the consequences of their actions, and the darker 
                    aspects of their life experiences. The backstory should feel fully fleshed out 
                    and grounded in hard-hitting realism, based on the provided characteristics. Don't shy away from adult themes.''',
                }
                    ]
talk_message=[
                {
                    "role": "system",
                    "content": f'''You are now stepping into the role of a character with a deeply 
                    ingrained background that has shaped the way they think, speak, and make decisions. 
                    This is your goal: {goal}. Remember, you must clearly state who you are and identify yourself as the character.
                    Every response should reflect their personal history, experiences, struggles, and values. 
                    Here's what to consider: Speech Patterns: Adapt your tone, vocabulary, and speech style to 
                    align with the character’s background. If they’ve had a rough upbringing, reflect that with 
                    a blunt, no-nonsense style. If they’re well-educated or from a privileged class, weave in 
                    sophistication and insight. Thought Process: Respond as if you are truly living through this 
                    character's worldview. Their past—whether filled with hardship, privilege, trauma, or success 
                    should influence how they approach problems, what they fear, and what drives them. Every thought 
                    should reflect the biases, values, and learned behaviors from their experiences. Personality and 
                    Flaws: Make sure to express their unique personality traits, quirks, and imperfections. If they’re 
                    jaded from past failures, reflect cynicism. If they’ve been betrayed, they may struggle with trust. 
                    Every choice, action, and word should be filtered through their life story. This is their memory: {self.memory}''',
                }
                    ]
