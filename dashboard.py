import pandas as pd
import streamlit as st
import warnings
from streamlit_option_menu import option_menu
import plotly.express as px
import ast
warnings.filterwarnings('ignore')
df = pd.read_csv('airbnb.csv')


def header():
    head1, head2, head3 = st.columns([3, 3, 1.5])
    with head2:
        # st.title('Industrial Copper Modeling')
        st.markdown(
            "<h2 style= 'color: #F4511E;font-size: 48px;font-weight :900'><b>Airbnb Analysis</b></h2>",
            unsafe_allow_html=True)


def option_container():
    left, optioncontainer, right = st.columns([0.2, 3, 0.2])
    with optioncontainer:
        selected = option_menu(menu_title='', options=['Home', 'Analysis', 'Geo'],
                               icons=['house', 'graph-up-arrow', 'globe2'], orientation='horizontal')
        return selected

def home():
    import streamlit as st
    st.title("Airbnb")
    airbnb_paragraph = """
    <p style="font-size: 18px;">Airbnb is an online marketplace and hospitality platform that allows individuals to rent or lease short-term lodging in private residences, such as homes, apartments, rooms, or even unique accommodations like treehouses or castles. Founded in 2008, Airbnb has become a global platform that connects hosts (property owners or renters) with guests (travelers or people seeking short-term accommodations).</p>
    <p style="font-size: 18px;">Here's how Airbnb typically works:</p>
    <ul>
        <li style="font-size: 17px;">Hosts: People who have available space to rent list their properties on Airbnb. These listings can range from spare rooms in their homes to entire houses or apartments. Hosts set the price, availability, and house rules for their listings.</li>
        <li style="font-size: 17px;">Guests: Travelers or those in need of short-term lodging can browse listings on Airbnb's website or app. They can specify their travel dates, location preferences, and other criteria to find suitable accommodations.</li>
        <li style="font-size: 17px;">Booking: Guests can review the available listings, read reviews and descriptions, and communicate with hosts if they have questions. Once they find a suitable option, they can make a reservation through the platform.</li>
        <li style="font-size: 17px;">Payment: Airbnb facilitates the financial transactions, and guests typically pay through the platform. Hosts receive their payment after the guest's stay begins.</li>
        <li style="font-size: 17px;">Stay: Guests stay in the accommodations as arranged, and hosts are responsible for providing a clean and comfortable environment. Airbnb encourages open communication between hosts and guests during the stay to address any questions or issues.</li>
        <li style="font-size: 17px;">Review: After the stay, both hosts and guests can leave reviews and ratings for each other, contributing to building trust within the Airbnb community.</li>
    </ul>
    <p style="font-size: 18px;">Airbnb has disrupted the traditional hospitality industry by providing an alternative to hotels and enabling individuals to earn income from their available space. Regulations and policies regarding Airbnb vary by location, and in some places, there are legal restrictions on short-term rentals. Therefore, it's essential for both hosts and guests to be aware of local rules and regulations when using the platform.</p>
    """

    st.markdown(airbnb_paragraph, unsafe_allow_html=True)


def analysis():
    head1, head2, head3 = st.columns([1, 3.5, 1])
    with head2:
        analysis_option = option_menu(menu_title='', icons=['globe2', 'house-fill', 'sort-numeric-up', 'building'],
                               options=['Country', 'Property Type', 'Accommondate', 'Amentities'],
                               orientation='horizontal')
    if analysis_option == 'Country':
        st.markdown('#')
        head1, head2 = st.columns([3, 2])
        with head1:
            st.markdown('#')
            bar = px.bar(df, x='Price', y='Country')
            st.plotly_chart(bar)
        with head2:
            fig = px.pie(df, values='Price', names='Country', labels='Country', hole=.4, height=500, width=500)
            st.plotly_chart(fig)
    elif analysis_option == 'Property Type':
        st.markdown('#')
        head1, head2 = st.columns([3, 2])
        with head1:
            st.markdown('#')
            bar = px.area(df, x='Property Type', y='Price')
            st.plotly_chart(bar)
        with head2:
            fig = px.pie(df, values='Price', names='Property Type', labels='Property Type', hole=.4, height=500, width=500)
            st.plotly_chart(fig)
    elif analysis_option == 'Accommondate':
        st.markdown('#')
        head1, head2 = st.columns([3, 2])
        with head1:
            st.markdown('#')
            bar = px.bar(df, x='Price', y='Accommondate')
            st.plotly_chart(bar)
        with head2:
            fig = px.pie(df, values='Accommondate', names='Country', labels='Country', hole=.4, height=500, width=500)
            st.plotly_chart(fig)
    elif analysis_option == 'Amentities':
        st.markdown('#')
        dic={}
        new_dic={}
        for value in df['Amentities']:
            for lst in ast.literal_eval((value)):
                if lst not in dic:
                    dic[lst]=[]
                dic[lst].append(1)
        for key,value in dic.items():
            count=0
            for i in value:
                count+=1
            new_dic[key]=count
        filt_lst=[{key: val} for key,val in new_dic.items() if val>2500]
        amentities=[]
        counts=[]
        for i in filt_lst:
            for key,val in i.items():
                amentities.append(key)
                counts.append(val)
        final_dic={"Amentities":amentities,"Count":counts}
        am_c=pd.DataFrame(final_dic)
        head1, head2 = st.columns([3, 2])
        with head1:
            st.markdown('#')
            bar = px.funnel(data_frame=am_c, x='Amentities', y='Count')
            st.plotly_chart(bar)
        with head2:
            fig = px.pie(df, values=counts, names=amentities, labels=amentities, hole=.4, height=500, width=500)
            st.plotly_chart(fig)


def geo():
    head1, head2, head3 = st.columns([1, 3.5, 1])
    with head2:
        geo_option = option_menu(menu_title='', icons=['cash-coin', 'person-fill', 'people-fill', 'person-plus'],
                                  options=['Price', 'Review', 'Guest', 'Extra People'],
                                  orientation='horizontal')
    if geo_option=='Price':
        head1, head2, head3 = st.columns([0.6,3,1])
        country=[]
        for i in df['Country']:
            country.append(i)
        country=list(set(country))
        country.sort()
        lat=[-33.865143,14.2350,62.2270,35.0000,22.302711,38.736946,40.4637,39.1667,38.889805]
        lon=[151.209900,51.9253,105.3809,103.0000,114.177216,-9.142685,3.7492,35.6667,-77.009056]
        c_df=df.groupby('Country')['Price'].sum().reset_index()
        c_df['lat']=lat
        c_df['lon']=lon
        fig = px.scatter_geo(c_df, size='Price', lat=lat, lon=lon, color='Price', hover_name='Country'
                             , size_max=20, width=1000, height=1000,
                             color_continuous_scale=["orange", "yellow", "red"],projection="natural earth")
        with head2:
            st.plotly_chart(fig)
    elif geo_option=='Review':
        head1, head2, head3 = st.columns([0.6,3,1])
        country=[]
        for i in df['Country']:
            country.append(i)
        country=list(set(country))
        country.sort()
        lat=[-33.865143,14.2350,62.2270,35.0000,22.302711,38.736946,40.4637,39.1667,38.889805]
        lon=[151.209900,51.9253,105.3809,103.0000,114.177216,-9.142685,3.7492,35.6667,-77.009056]
        c_df=df.groupby('Country')['N_Reviews'].sum().reset_index()
        c_df['lat']=lat
        c_df['lon']=lon
        fig = px.scatter_geo(c_df, size='N_Reviews', lat=lat, lon=lon, color='N_Reviews', hover_name='Country'
                             , size_max=20, width=1000, height=1000,
                             color_continuous_scale=["orange", "yellow", "red"],projection="natural earth")
        with head2:
            st.plotly_chart(fig)
    elif geo_option=='Guest':
        head1, head2, head3 = st.columns([0.6,3,1])
        country=[]
        for i in df['Country']:
            country.append(i)
        country=list(set(country))
        country.sort()
        lat=[-33.865143,14.2350,62.2270,35.0000,22.302711,38.736946,40.4637,39.1667,38.889805]
        lon=[151.209900,51.9253,105.3809,103.0000,114.177216,-9.142685,3.7492,35.6667,-77.009056]
        c_df=df.groupby('Country')['Guests'].sum().reset_index()
        c_df['lat']=lat
        c_df['lon']=lon
        fig = px.scatter_geo(c_df, size='Guests', lat=lat, lon=lon, color='Guests', hover_name='Country'
                             , size_max=20, width=1000, height=1000,
                             color_continuous_scale=["orange", "yellow", "red"],projection="natural earth")
        with head2:
            st.plotly_chart(fig)

    elif geo_option=='Extra People':
        head1, head2, head3 = st.columns([0.6,3,1])
        country=[]
        for i in df['Country']:
            country.append(i)
        country=list(set(country))
        country.sort()
        lat=[-33.865143,14.2350,62.2270,35.0000,22.302711,38.736946,40.4637,39.1667,38.889805]
        lon=[151.209900,51.9253,105.3809,103.0000,114.177216,-9.142685,3.7492,35.6667,-77.009056]
        c_df=df.groupby('Country')['Extra People'].sum().reset_index()
        c_df['lat']=lat
        c_df['lon']=lon
        fig = px.scatter_geo(c_df, size='Extra People', lat=lat, lon=lon, color='Extra People', hover_name='Country'
                             , size_max=20, width=1000, height=1000,
                             color_continuous_scale=["orange", "yellow", "red"],projection="natural earth")
        with head2:
            st.plotly_chart(fig)