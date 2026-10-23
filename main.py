from dash import Dash, dcc, html, Input, Output, ctx
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify


# =========================================================
# COUNTRY LIST
# =========================================================

countries = [
    "Argentina",
    "Bolivia",
    "Brazil",
    "Chile",
    "Colombia",
    "Ecuador",
    "Guyana",
    "Paraguay",
    "Peru",
    "Suriname",
    "Uruguay",
    "Venezuela",
]


# =========================================================
# ISO-3 COUNTRY CODES
# =========================================================

country_codes = {
    "Argentina": "ARG",
    "Bolivia": "BOL",
    "Brazil": "BRA",
    "Chile": "CHL",
    "Colombia": "COL",
    "Ecuador": "ECU",
    "Guyana": "GUY",
    "Paraguay": "PRY",
    "Peru": "PER",
    "Suriname": "SUR",
    "Uruguay": "URY",
    "Venezuela": "VEN",
}


# =========================================================
# COUNTRY INFORMATION
# =========================================================

category_descriptions = {
    "Campaign Music": (
        "Referred to in South America as ''jingle político'' (political jingle) or ''tema de campaña'' "
        "(campaign theme), campaign music plays an important role in spreading the word for political movements "
        "and candidates. Beyond simple political advertisement, campaign music often takes a "
        "life of its own in populist movements, being sung by supporters in political "
        "rallies and other campaign events."
    ),
    "Sports": (
        "Identifying whether sports are used for national unity versus populist  "
        "means is a difficult task. Attending a sporting event is common amongst both "
        "populists and non-populists, sometimes even as a form of international diplomacy. "
        "To make a distinction, this category includes instances of "
        "populists using athlete endorsements for political gain, or presenting themselves as "
        "representatives or members of sporting teams. Thus, shifting the emphasis away from "
        "the nation and the sport towards themselves."
    ),
    "Artificial Intelligence": (
        "Whether to promote a policy, self-aggrandize, or attack political opponents,  "
        "The use of artificial intelligence by populists is widespread in South America. "
        "While used by candidates and their supporters, this section will only look at "
        "instances of AI used officially used by candidates and their campaigns, allowing "
        "us to analyze how candidates present themselves when the limit is only a text prompt."
    ),
    "Leader Profile": (
        "A short description of selected populist leaders across South America, describing their "
        "background and context of their present policies."
    ),
}

country_data = {

    "Argentina": {
        "leader": {
            "name": "Javier Milei",
            "image": "/Assets/Milei_Presidente.jpg",
            "position": "center top",
        },

        "Leader Profile": "A self-described libertarian, Javier Milei is an economist who "
        "currently serves as the President of Argentina for the 2023-2027 cycle. "
        "Famous for using a chainsaw as a prop on the campaign trail, he proposed dollarizing "
        "the Argentinian economy and cutting "
        "down on government spending to curb rising inflation. Milei also adopted the symbol of the "
        "lion throughout his campaign, stating that he ''did not come to lead sheep, but to awaken lions.'' ",


        "Campaign Music": [
            {
                "title": "La Marcha del Leon - Juan Pablo Gariglio",
                "url": "https://www.youtube.com/watch?v=hEk5Mc8j-OM",
                "description": "The Lion's March, as it's called in English, is more of a political song "
                "than a traditional political jingle. Composed by Juan Pablo Gariglio as a traditional "
                "Argentinian rock song, it sounds like something that could play on a radio in Buenos Aires. "
                "However, the political connection is clear. The song states that it will tell the ''story of "
                "a place that was sentenced to death... whose liberty of yesteryear was in the hands of tyrants "
                "and ogres.'' It wasn't until Milei, ''a light of freedom that began to awaken lions.'' that the "
                "place was saved. ",
            },
        ],

        "Sports": [
            {
                "title": "Viva la Argentina",
                "url": "https://www.instagram.com/p/DbIuQPuTxnJ/",
                "description": "An AI-generated image of Milei wearing Argentina's football jersey. "
                "Posted 4 days after the final of the World Cup, where Argentina fell against Spain. "
                "The image shows Milei opening his suit to reveal the shirt, reminiscent of how "
                "Superman reveals his costume in the comics. Along with the phrase ''long live Argentina, "
                "Damn it'' it shows him as an unapologetic hero of his country.",
            },
        ],

        "Artificial Intelligence": [
            {
                "title": "Argentina Week Paris",
                "url": "https://www.instagram.com/reel/Dd33EjwTgBV/",
                "description": "An AI generated short video of Milei standing on top of the Eiffel tower. "
                "He can be seen holding the Argentinian flag, with a lion climbing the tower to sit next "
                "to him. The video was promotional material for the first Argentina Week in Paris, an event "
                "which sought to promote trade and investment in Argentina's energy sectors."
            },
            {
                "title": "La Libertad Avanza",
                "url": "https://www.instagram.com/p/DY9z9VyTFJV/",
                "description": "While it could fall under the political jingle category, this AI generated "
                "music video was posted by Milei while already in office. In it, Milei flaunts about the "
                "economic accomplishments of his administration. Among them, he claims to have ''brought "
                "down the reds,'' and to have ''removed those that lived from corruption.'' The song ends "
                "stating ''Milei did it,'' as you can see him being carried in the arms of the Argentinian "
                "people in celebration. ",
            }
        ],

    },


    "Bolivia": {

        "Campaign Music": [],

        "Leader Profile": "",

        "Sports": [],

        "Artificial Intelligence": [],

    },


    "Brazil": {
        "leader": {
            "name": "Flávio Bolsonaro",
            "image": "/Assets/Flavio_Presidente.jpg",
            "position": "center top",
        },

        "Leader Profile": "The eldest son of disgraced former President Jair Bolsonaro, "
        "Flávio Bolsonaro is the leading candidate to win the upcoming second round of the "
        "2026 Brazilian elections. Flávio is a critic of the Supreme Court, which sentenced his father "
        "to 27 years in prison for a failed Coup d'état in 2023. He has also made security a key "
        "issue in his campaign, speaking out against rising crime rates in the Lula administration.",

        "Campaign Music": [
            {
                "title": "O Brasil Tem Futuro",
                "url": "https://www.youtube.com/shorts/f7LBxbijOEQ",
                "description": "The simplest of all of the political jingles in this collection. "
                "The jingle begins with ''let's enter with the right foot, so that Brazil has a future.'' "
                "Another line states ''with the people coming together, we will bring Brazil to the right path.'' "
                "The message of the jingle is two sided. It portrays Flávio Bolsonaro as the ''right'' choice "
                "for president who also happens to be the right-wing candidate."
            },
        ],

        "Sports": [
            {
                "title": "Flavio and Supporters with Amarelinha",
                "url": "https://www.instagram.com/p/DdjsZHDJT0-/",
                "description": "Flávio Bolsonaro's father, Jair Bolsonaro, was the pioneer in the use of "
                "football jerseys in South America as a political symbol. Called the ''amarelinha,'' the "
                "jersey of the Brazilian national team is used by the Brazilian right as a form of uniform, "
                "worn at political rallies, protests, and while voting. As a national symbol, it connects "
                "the rights ideology with national pride and the victorious history of the Brazilian national "
                "football team.",
            }
        ],

        "Artificial Intelligence": [
            {
                "title": "Você sente essa dor?...",
                "url": "https://www.instagram.com/p/DdwD3RqpxHT/?hl=en",
                "description": "An AI generated video telling the story of a family living in a Brazilian "
                "''favela,'' (an impoverished neighborhood or slum). The video highlights the reality of "
                "gang violence in Brazil, as a small shop owner is killed by gang members in front of "
                "a kid who sees him as a friend. The video then shows the kid starting to work for the gang "
                "himself, showing the cyclical nature of violence. However, inspired by his sister, who "
                "was assaulted by a gang member, he chose to break the cycle and not remain in the gang. "
                "The video ends with the kid and his family putting up posters in support of Bolsonaro, "
                "portraying him as the solution to security issues in the country. ",
            },
            {
                "title": "Flávio Muppets Style",
                "url": "https://www.instagram.com/p/Dcq82bXp7j0/",
                "description": "An AI generated music video in the style of the muppets. The genre of the music "
                " in the video is a traditional Brazilian ''sertanejo.'' Anti-establishment and anti-elite "
                "imagery is shown in the video, stating that Brazil has had ''enough of befitting bandits'' "
                "and that those who ''steal their place is in jail.'' Interestingly, the muppets in jail "
                "are holding up an L sign with their hands, a symbol of the incumbent Lula campaign.",
            }
        ],

    },


    "Chile": {
        "leader": {
            "name": "José Antonio Kast",
            "image": "/assets/Kast_Presidente.png",
            "position": "center top",
        },

        "Leader Profile": "A lawyer, former congressman, father of 9, and son of of a German immigrant "
        "who was a member of the Nazi party, José Antonio Kast is the President of Chile for the "
        "2026-2030 term. A conservative, Kast ran on an anti-immigration platform and has praised "
        "El Salvador's Nayib Bukele's ''strong hand'' approach on security. He has also "
        "suggested the creation of an Immigration and Customs Enforcement (ICE) like agency in Chile "
        "to support his security agenda.",

        "Campaign Music": [
            {
                "title": "Vota 5 por Kast",
                "url": "https://www.youtube.com/watch?v=VuWdJHEW7a8",
                "description": "A traditional political jingle, with a clear message and call to action. "
                "The chorus invites people to ''vote 5 for Kast,'' which was the candidate's number "
                "in the ballot. Curiously, it includes ''without communism, without communism'' as "
                "part of its messaging, showing how Kast's campaign was trying to portray his opponents.",
            },
        ],

        "Sports": [],

        "Artificial Intelligence": [
            {
                "title": "Escudo Fronterizo",
                "url": "https://www.instagram.com/p/DQZZnEdke2w/?hl=en",
                "description": "A simple AI generated video introducing Kast's plan for a "
                "''border shield'' to crack down on illegal immigration into Chile. The video is in the "
                "style of a hard rock concert, where the singer states ''those who do not comply, "
                "cannot pass,'' portraying a strong immigration policy. Interestingly, the ''border shield'' "
                "initiative was introduced through this simple AI post, with a more in depth description "
                "of the plan posted hours later.",
            }
        ],

    },


    # =====================================================
    # COLOMBIA
    # =====================================================

    "Colombia": {

        # Leader information
        "leader": {
            "name": "Abelardo de la Espriella",
            "image": "/assets/Abelardo_Presidente.jpg",
            "position": "center top",
        },

        "Leader Profile":
            "Calling himself ''El Tigre;'' political outsider, entrepreneur, and lawyer "
            "Abelardo de la Espriella (ADLE) became the President of Colombia for the 2026-2030 term. "
            "By rejecting to govern with the political establishment and drawing on Colombian patriotism "
            "with his political party ''Defenders of the Homeland,'' ADLE ran a campaign focused on "
            "national security that rejected the peace process from the previous administration. ",

        "Campaign Music": [

            {
                "title": "El Tigre de la Patria - Nicolas Tovar",
                "url": "https://www.youtube.com/watch?v=STOfx5VI0Dk",
                "description": "The official anthem of ADLE's campaign, created by Colombian artist "
                "Nicolás Tovar. It's chorus repeats: ''The tiger that roars and bites. "
                " The tiger who fears nothing. The tiger who leaves a mark, Abelardo de la Espriella.'' "
                "The music video also shows ADLE reading the bible and looking up at the sky as a "
                "light shines from the heavens, as if chosen by God to lead the country.",
            },

            {
                "title": "Tigre de mi Vida - Abelardo y la Manada",
                "url": "https://www.youtube.com/watch?v=AfNbmfmtCcQ",
                "description": "Designed by Andrés Gelvez, a political consultant for ADLE, using AI. "
                "The song is based on a chant he heard while attending a watch party of the "
                "country's national football league. The song repeats ''tiger of my life... let's win "
                "against Petro, for our nation.''"
            },


        ],

        "Sports": [
            {
                "title": "Call with Nairo Quintana and Miguel Angel Borja",
                "url": "https://www.instagram.com/p/DZfpS-kNEVD/?hl=en",
                "description": "In this video, ADLE can be seen wearing the Colombian national football team jersey, "
                "a political symbol of his campaign (a strategy was borrowed from Bolsonarism in Brazil). "
                "He also shows himself on the phone with Nairo Quintana, a world renowned Colombian cyclist. He also "
                "shows his call with Miguel Angel Borja, a Colombian footballer who represented Colombia in the 2018 "
                "World Cup. Both pledge their support to him, stating that they are ''standing firm with the "
                "motherland,'' ADLE's political slogan.",
            },
        ],

        "Artificial Intelligence": [
            {
                "title": "Enrique Serrano López, Asesor Presidencial de la Patria Milagro",
                "url": "https://www.instagram.com/reel/DbHQEVAvoGL/",
                "description": "After being elected, ADLE announced his presidential cabinet through the "
                "social media posts generated by AI. This is one example of the many AI cabinet announcements. "
                "A constant in all of the cabinet announcement videos is the tiger, which represents ADLE, and "
                " the mention of the ''miracle homeland.'' The miracle homeland is the name given by ADLE to his "
                "presidential term, where the change that will be achieved was believed to be unobtainable. It also"
                "shows Enrique Serrano López declaring ''standing firm with the motherland,'' ADLE's political "
                "slogan, a form of declaring fealty to the political movement and the President.",
            },
        ],

    },


    "Ecuador": {

        "Leader Profile": "",

        "Campaign Music": [],

        "Sports": [],

        "Artificial Intelligence": [],

    },


    "Guyana": {

        "Campaign Music": [],

        "Leader Profile": "",

        "Sports": [],

        "Artificial Intelligence": [],

    },


    "Paraguay": {

        "Campaign Music": [],

        "Leader Profile": "",

        "Sports": [],

        "Artificial Intelligence": [],

    },


    "Peru": {
        "leader": {
            "name": "Keiko Fujimori",
            "image": "/assets/Fujimori_Presidente.jpg",
            "position": "center top",
        },

        "Leader Profile":
            "Keiko Fujimori is the "
            "President of Peru for the 2026-2031 term and is the 10th person in a decade to hold the title, "
            "The daughter of former Peruvian dictator Alberto Fujimori, she attempted on 4 "
            "different occasions to win the presidency campaigning on her father's anti-communist and "
            "tough on crime stance. She is accused by critics of leading-by-proxy during the previous "
            "administration b using her party's majority in congress for self gain, undermining the "
            "independence of this body.",

        "Campaign Music": [
            {
                "title": "El Ritmo de la China",
                "url": "https://www.youtube.com/watch?v=UYp76XpegkA",
                "description": "Despite being of Japanese ancestry, Keiko Fujimori's jingle "
                "is titled ''El Ritmo de la China'' (The Chinese woman's rhythm). Originally "
                "created for her father's 2000 presidential reelection bid, Keiko's remix "
                "declares that ''the antis had their chance, those who hated had their chance, here "
                "comes Keiko to put order to what they couldn't.'' "
            },

        ],

        "Sports": [],

        "Artificial Intelligence": [
            {
                "title": "Keiko Contra la Anemia",
                "url": "https://www.instagram.com/reel/DYr9UHRAt6U/?hl=en",
                "description": "Keiko Fujimori's approach to AI is different from her counterparts. "
                "She uses AI alongside her speeches, using her own voice to spread her message while "
                "using AI to visualize her arguments. In this video, she is describing how her government "
                "will give subsidies to community run cafeterias as a method of tackling anemia in "
                "Peruvian children. Instead of the AI video speaking for her, it serves as an aid of what "
                "the program would look like if she is elected.",
            }
        ],

    },


    "Suriname": {

        "Leader Profile": "",

        "Campaign Music": [],

        "Sports": [],

        "Artificial Intelligence": [],

    },


    "Uruguay": {

        "Leader Profile": "",

        "Campaign Music": [],

        "Sports": [],

        "Artificial Intelligence": [],

    },


    "Venezuela": {

        "Leader Profile": "",

        "Campaign Music": [],

        "Sports": [],

        "Artificial Intelligence": [],

    },

}


# =========================================================
# CATEGORIES
# =========================================================

categories = [
    "Leader Profile",
    "Campaign Music",
    "Sports",
    "Artificial Intelligence",
]


# =========================================================
# CREATE MAP
# =========================================================

def create_map(selected_category):

    colors = []
    hover_text = []

    for country in countries:

        if selected_category == "Leader Profile":
            sources = country_data[country].get("Leader Profile", "")
            has_information = bool(sources.strip())
        else:
            sources = country_data[country][selected_category]
            has_information = len(sources) > 0

        # -------------------------------------------------
        # Country HAS information
        # -------------------------------------------------

        if has_information:

            colors.append(1)

            number_of_sources = len(sources)

            if selected_category == "Leader Profile":
                hover_text.append(
                    f"<b>{country}</b><br>"
                    "<span style='color:#2E86DE;'>"
                    "● Leader profile available"
                    "</span><br><br>"
                    "<i>Click to view profile</i>"
                )
            else:
                number_of_sources = len(sources)

                source_word = (
                    "source" if number_of_sources == 1 else "sources"
                )

                hover_text.append(
                    f"<b>{country}</b><br>"
                    "<span style='color:#2E86DE;'>"
                    "● Information available"
                    "</span><br>"
                    f"{number_of_sources} {source_word}<br><br>"
                    "<i>Click for sources</i>"
                )


        # -------------------------------------------------
        # Country DOES NOT have information
        # -------------------------------------------------

        else:

            colors.append(0)

            hover_text.append(

                f"<b>{country}</b><br>"
                f"<span style='color:#777;'>"
                f"● No information available yet"
                f"</span>"

            )


    # =====================================================
    # MAP
    # =====================================================

    fig = go.Figure(

        go.Choropleth(

            locations=[
                country_codes[country]
                for country in countries
            ],

            z=colors,

            text=countries,

            customdata=countries,

            locationmode="ISO-3",

            colorscale=[

                [0.00, "#D9D9D9"],
                [0.49, "#D9D9D9"],

                [0.50, "#2E86DE"],
                [1.00, "#2E86DE"],

            ],

            showscale=False,

            hovertext=hover_text,

            hovertemplate=(
                "%{hovertext}"
                "<extra></extra>"
            ),

            marker_line_color="white",

            marker_line_width=1.5,

        )

    )


    # =====================================================
    # MAP GEOGRAPHY
    # =====================================================

    fig.update_geos(

        scope="south america",

        showland=True,

        landcolor="#E8E8E8",

        showocean=True,

        oceancolor="#DFF3FF",

        showcountries=True,

        countrycolor="white",

        projection_type="natural earth",

    )


    # =====================================================
    # MAP LAYOUT
    # =====================================================

    fig.update_layout(

        margin=dict(
            l=0,
            r=0,
            t=10,
            b=0,
        ),

        height=680,

        paper_bgcolor="white",

        plot_bgcolor="white",

        clickmode="event",

    )


    return fig


# =========================================================
# DASH APPLICATION
# =========================================================

app = Dash(__name__)
server = app.server


# =========================================================
# APPLICATION LAYOUT
# =========================================================

app.layout = html.Div(

    [

        # =================================================
        # TITLE
        # =================================================

        html.H1(

            "Populism in South America, Leaders and Strategies",

            style={
                "textAlign": "center",
                "fontFamily": "Arial, sans-serif",
                "fontWeight": "600",
                "marginBottom": "5px",
            },

        ),


        html.P(

            "Explore the strategies and tools populist South American leaders use"
            "in and out of campaign to promote themselves and their movements.",

            style={
                "textAlign": "center",
                "fontFamily": "Arial, sans-serif",
                "color": "#666",
                "marginTop": "0",
                "marginBottom": "20px",
            },

        ),


        # =================================================
        # CATEGORY DROPDOWN
        # =================================================

        html.Div(

            [

                html.Label(

                    "Category",

                    style={
                        "fontFamily": "Arial, sans-serif",
                        "fontWeight": "bold",
                        "marginRight": "10px",
                    },

                ),


                dcc.Dropdown(

                    id="category-dropdown",

                    options=[

                        {
                            "label": category,
                            "value": category,
                        }

                        for category in categories

                    ],

                    value="Campaign Music",

                    clearable=False,

                    searchable=False,

                    style={
                        "width": "320px",
                        "display": "inline-block",
                        "fontFamily": "Arial, sans-serif",
                    },

                ),

            ],

            style={
                "display": "flex",
                "justifyContent": "center",
                "alignItems": "center",
                "marginBottom": "10px",
            },

        ),
            html.Div(
            id="category-description-box",
            children=category_descriptions["Campaign Music"],
            style={
                "width": "90%",
                "margin": "15px auto",
                "padding": "15px 20px",
                "backgroundColor": "#F4F6F8",
                "border": "1px solid #D9DEE5",
                "borderRadius": "10px",
                "color": "#333333",
                "fontSize": "16px",
                "lineHeight": "1.6",
                "boxSizing": "border-box",
                "fontFamily": "Arial, sans-serif",
            },
        ),

        # =================================================
        # LEGEND
        # =================================================

        html.Div(

            [

                html.Span(

                    "●",

                    style={
                        "color": "#2E86DE",
                        "fontSize": "24px",
                        "verticalAlign": "middle",
                    },

                ),

                html.Span(

                    " Information available",

                    style={
                        "fontFamily": "Arial, sans-serif",
                        "marginRight": "20px",
                    },

                ),


                html.Span(

                    "●",

                    style={
                        "color": "#D9D9D9",
                        "fontSize": "24px",
                        "verticalAlign": "middle",
                    },

                ),

                html.Span(

                    " No information yet",

                    style={
                        "fontFamily": "Arial, sans-serif",
                    },

                ),

            ],

            style={
                "textAlign": "center",
                "marginBottom": "5px",
            },

        ),


        # =================================================
        # MAIN CONTENT
        #
        # Map + information panel
        # =================================================

        html.Div(

            [

                # -----------------------------------------
                # MAP
                # -----------------------------------------

                html.Div(

                    [

                        dcc.Graph(

                            id="south-america-map",

                            figure=create_map(
                                "Campaign Music"
                            ),

                            config={
                                "displayModeBar": True,
                                "scrollZoom": False,
                            },

                            style={
                                "width": "100%",
                            },

                        ),

                    ],

                    style={
                        "width": "70%",
                    },

                ),


                # -----------------------------------------
                # INFORMATION PANEL
                # -----------------------------------------

                html.Div(

                    id="information-panel",

                    children=[

                        html.H3(
                            "Select a country",
                            style={
                                "fontFamily":
                                    "Arial, sans-serif",
                            },
                        ),

                        html.P(

                            "Countries highlighted in blue "
                            "have information available. "
                            "Click one to see its sources.",

                            style={
                                "fontFamily":
                                    "Arial, sans-serif",
                                "color": "#666",
                                "lineHeight": "1.5",
                            },

                        ),

                    ],

                    style={

                        "width": "30%",

                        "minHeight": "400px",

                        "backgroundColor": "#F7F7F7",

                        "borderRadius": "10px",

                        "padding": "25px",

                        "boxSizing": "border-box",

                        "fontFamily":
                            "Arial, sans-serif",

                    },

                ),

            ],

            style={

                "display": "flex",

                "alignItems": "flex-start",

                "gap": "10px",

            },

        ),

    ],

    style={

        "maxWidth": "1200px",

        "margin": "0 auto",

        "padding": "20px",

        "backgroundColor": "white",

    },

)


# =========================================================
# UPDATE MAP WHEN CATEGORY CHANGES
# =========================================================

@app.callback(

    Output(
        "south-america-map",
        "figure",
    ),

    Input(
        "category-dropdown",
        "value",
    ),

)

def update_map(selected_category):

    return create_map(selected_category)

@app.callback(
    Output("category-description-box", "children"),
    Input("category-dropdown", "value"),
)
def update_category_description(selected_category):
    return category_descriptions.get(
        selected_category,
        "Select a category to see its description."
    )
# =========================================================
# COUNTRY INFORMATION PANEL
# =========================================================

@app.callback(

    Output(
        "information-panel",
        "children",
    ),

    Input(
        "south-america-map",
        "clickData",
    ),

    Input(
        "category-dropdown",
        "value",
    ),

)

def update_information_panel(
    click_data,
    selected_category,
):

    # -----------------------------------------------------
    # If the user changes category, reset the panel.
    # -----------------------------------------------------

    if ctx.triggered_id == "category-dropdown":

        return [

            html.H3(
                "Select a country",
                style={
                    "marginTop": "0",
                },
            ),

            html.P(

                f"Select a blue country to see "
                f"{selected_category} sources.",

                style={
                    "color": "#666",
                    "lineHeight": "1.5",
                },

            ),

        ]


    # -----------------------------------------------------
    # Nothing has been clicked
    # -----------------------------------------------------

    if not click_data:

        return [

            html.H3(
                "Select a country",
                style={
                    "marginTop": "0",
                },
            ),

            html.P(

                f"Select a blue country to see "
                f"{selected_category} sources.",

                style={
                    "color": "#666",
                    "lineHeight": "1.5",
                },

            ),

        ]


    # -----------------------------------------------------
    # Determine clicked country
    # -----------------------------------------------------

    try:

        country = (
            click_data["points"][0]["customdata"]
        )

    except (KeyError, IndexError, TypeError):

        return html.P(
            "Unable to identify the selected country."
        )


    # -----------------------------------------------------
    # Get country information
    # -----------------------------------------------------

    country_info = country_data[country]

    sources = country_info[selected_category]


    # =====================================================
    # LEADER SECTION
    # =====================================================

    leader_section = []

    if "leader" in country_info:

        leader = country_info["leader"]

        leader_section = [

            html.Img(

                src=leader["image"],

                style={

                    "width": "180px",

                    "height": "180px",

                    "objectFit": "cover",

                    "objectPosition": leader.get("position", "center center"),

                    "borderRadius": "50%",

                    "display": "block",

                    "margin": "0 auto 15px auto",

                },

            ),

            html.H3(

                leader["name"],

                style={

                    "textAlign": "center",

                    "marginTop": "0",

                    "marginBottom": "20px",

                },

            ),
        ]

        # -----------------------------------------------------
        # LEADER PROFILE
        # -----------------------------------------------------

        if selected_category == "Leader Profile":

            profile = country_info.get("Leader Profile", "").strip()

            if not profile:
                return leader_section + [
                    html.H2(
                        country,
                        style={"marginTop": "0"},
                    ),
                    html.P(
                        "No leader profile is available yet.",
                        style={
                            "color": "#777",
                            "lineHeight": "1.5",
                        },
                    ),
                ]

            return leader_section + [
                html.H2(
                    country,
                    style={"marginTop": "0"},
                ),
                html.H4(
                    "Leader Profile",
                    style={
                        "color": "#666",
                        "fontWeight": "normal",
                    },
                ),
                html.P(
                    profile,
                    style={
                        "color": "#555",
                        "lineHeight": "1.6",
                        "fontSize": "14px",
                    },
                ),
            ]

    # -----------------------------------------------------
    # No information
    # -----------------------------------------------------

    if not sources:

        return leader_section + [

            html.H3(

                country,

                style={

                    "marginTop": "0",

                    "marginBottom": "5px",

                },

            ),

            html.H4(

                selected_category,

                style={

                    "color": "#666",

                    "fontWeight": "normal",

                },

            ),

            html.P(

                "There is no information available "
                "for this category yet.",

                style={

                    "color": "#777",

                    "lineHeight": "1.5",

                },

            ),

        ]

    # -----------------------------------------------------
    # Create clickable source list
    # -----------------------------------------------------

    source_elements = []

    for source in sources:
        source_elements.append(
            html.Div(
                [
                    # Clickable source title
                    html.A(
                        source["title"],
                        href=source["url"],
                        target="_blank",
                        rel="noopener noreferrer",
                        style={
                            "color": "#2E86DE",
                            "fontSize": "16px",
                            "fontWeight": "bold",
                            "textDecoration": "none",
                        },
                    ),

                    # Description underneath the title
                    html.P(
                        source.get(
                            "description",
                            "No description available yet."
                        ),
                        style={
                            "fontSize": "14px",
                            "color": "#555555",
                            "lineHeight": "1.5",
                            "marginTop": "6px",
                            "marginBottom": "0",
                        },
                    ),
                ],
                style={
                    "padding": "12px 0",
                    "borderBottom": "1px solid #DDDDDD",
                },
            )
        )


    # -----------------------------------------------------
    # Return panel
    # -----------------------------------------------------

    return leader_section + [

        html.H2(

            country,

            style={

                "marginTop": "0",

                "marginBottom": "5px",

            },

        ),

        html.H4(

            selected_category,

            style={

                "color": "#666",

                "fontWeight": "normal",

                "marginTop": "0",

                "marginBottom": "20px",

            },

        ),


        html.P(

            f"{len(sources)} "
            f"{'source' if len(sources) == 1 else 'sources'}",

            style={

                "color": "#777",

            },

        ),


        html.Div(source_elements),

    ]


# =========================================================
# RUN APPLICATION
# =========================================================

import os

if __name__ == "__main__":
    app.run(
        debug=False,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8050)),
    )
