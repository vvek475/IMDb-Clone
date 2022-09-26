from IMDb_clone.settings import API_KEY
import requests

BASE_URL='https://api.themoviedb.org/3'

movie_detail_url_segments={
    
    'CREDITS':'credits',
    'IMAGES':'images',
    'RECOMMENDATIONS':'recommendations',
    'SIMILAR':'similar',
    'VIDEOS':'videos',
    'WATCH_PROVIDERS':'watch/providers',
    
}

def movie_detail(id,title=None):
    
    url='' 
    
    if title is None:url= f'{BASE_URL}/movie/{id}?api_key={API_KEY}'
    
    else: url=f'{BASE_URL}/movie/{id}/{movie_detail_url_segments[title]}?api_key={API_KEY}'
    
    return url

movies={
    
    'GENRE':f'{BASE_URL}/trending/all/day?api_key={API_KEY}',
    'TRENDING_MOVIES':f'{BASE_URL}/trending/all/day?api_key={API_KEY}',
    'LATEST':f'{BASE_URL}/movie/latest?api_key={API_KEY}',
    'NOW_PLAYING':f'{BASE_URL}/movie/now_playing?api_key={API_KEY}',
    'TOP_RATED':f'{BASE_URL}/movie/top_rated?api_key={API_KEY}',
    'MOVIE':movie_detail
    
}


def get(url,*args,**kwargs):
    
    params=[f'&{key}={value}' for key,value in kwargs.items()]
    params=('').join(params)
    response=requests.get(f'{url}{params}')
    
    return response.json()