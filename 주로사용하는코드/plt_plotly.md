<br>

#### 1. 시각화_판다스 - 시각화(plotly)

<br>

# 시각화(plotly)

<br>

## 1. 공간분석 - 시각화 


### 1. 공간 분석 

<br>

```py
# 설치 
# pip install plotly
import plotly.express as px


fig = px.scatter_mapbox(df_caffee, lat="위도", lon="경도", hover_name="상호명", hover_data=["지번주소", "도로명주소"],
                        color_discrete_sequence=["#636EFA"], zoom=11, height=600)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

```

<br>

### 2. 공간 정보 오픈 플랫폼 

공간정보 오픈 프랫폼을 사용하기위해서는 필요함 -> [open api 발급](http://www.vworld.kr/dev/v4api.do)


<br>

```py

# VworldSatellite, VworldHybrid 타일 추가

fig = px.scatter_mapbox(df_caffee, lat="위도", lon="경도", hover_name="상호명", hover_data=["지번주소", "도로명주소"],
                        color_discrete_sequence=["#FFA15A"], zoom=11, height=600)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# 개인 api 코드 있음 
fig.update_layout(
    mapbox_style="white-bg",
    mapbox_layers=[
        {
            "below": 'traces', 
            "sourcetype": "raster",
            "source": [
                "http://api.vworld.kr/req/wmts/1.0.0/개인키입력/Satellite/{z}/{y}/{x}.jpeg"
            ]
        },
        {
            "sourcetype": "raster",
            "source": [
                "http://api.vworld.kr/req/wmts/1.0.0/개인키입력/Hybrid/{z}/{y}/{x}.png"
            ],
        }
      ])
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

```

<br>


## 3. 맵박스 밀도 열지도

<br>

```py

# 맵박스 밀도 열지도
import plotly.graph_objects as go

fig = go.Figure(go.Densitymapbox(lat=df_caffee['위도'], lon=df_caffee['경도'], radius=10))
fig.update_layout(
    mapbox_style="white-bg",
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "source": [
                "http://api.vworld.kr/req/wmts/1.0.0/개인키입력/Satellite/{z}/{y}/{x}.jpeg"
            ]
        },
        {
            "sourcetype": "raster",
            "source": [
                "http://api.vworld.kr/req/wmts/1.0.0/개인키입력/Hybrid/{z}/{y}/{x}.png"
            ],
        }
      ],
    mapbox_zoom=9,
    mapbox_center = {"lat": 35.14, "lon": 129.07}) 
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

```

<br>





## 3. 

<br>

```py



```

<br>





## 3. 웹으로 그래프 보이기 

<br>

```py

import plotly.graph_objects as go # or plotly.express as px
fig = go.Figure() # or any Plotly Express function e.g. px.bar(...)
# fig.add_trace( ... )
# fig.update_layout( ... )

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter

```

<br>







<br>

---

<br>

## Reference <br>

- Plotly 참고자료_지구과학, GIS, 그리고 원격탐사 블로그입니다.ㅍ &nbsp; : &nbsp;<http://blog.daum.net/geoscience/1420> <br>
- Plotly 참고자료_하나씩 점을 찍어 나가며 &nbsp; : &nbsp;<https://dailyheumsi.tistory.com/118> <br>
<br>
<br>

## Practice makes perfect! <br>

- [내용](주소)