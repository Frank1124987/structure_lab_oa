import pandas as pd
import plotly.express as px
from preswald import connect, get_df, query
from preswald import table, text, plotly

''' Load dataset '''
connect()  # Initialize connection to preswald.toml data sources
df = get_df("spotify_csv")  # Load data

''' Query '''
sql = """
    SELECT 
        artist_name, 
        MAX(CAST(followers as INT)) as followers,
        AVG(CAST(track_popularity as INT)) as avg_track_popularity
    FROM spotify_csv 
    GROUP BY artist_name
    ORDER BY followers DESC
    LIMIT 20;
"""
filtered_df = query(sql, "spotify_csv")

fig = px.scatter(filtered_df, x='avg_track_popularity', y='followers', text='artist_name',
                 title='avg_track_popularity vs. followers')
fig.update_traces(textposition='top center', marker=dict(size=12, color='lightblue'))
fig.update_layout(template='plotly_white')


text("# Followers vs Average Track Popularity")
plotly(fig)
table(filtered_df, title="Filtered Data")
