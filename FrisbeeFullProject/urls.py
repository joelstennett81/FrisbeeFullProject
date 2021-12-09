from django.urls import path
from FrisbeeApp.views import game_views as game, home_page_views as home_page, league_views as league, player_game_views as player_game, player_views as player, team_views as team
urlpatterns = [
    path('', home_page.home_page_view, name='home_page'),
    path('game/', game.list_view, name='game_list'),
    path('game+<id>/', game.detail_view, name='game_detail'),
    path('game/create/', game.create_view, name='game_create'),
    path('game/update+<id>/', game.update_view, name='game_update'),
    path('league/', league.list_view, name='league_list'),
    path('league+<id>/', league.detail_view, name='league_detail'),
    path('league/create/', league.create_view, name='league_create'),
    path('league/update+<id>/', league.update_view, name='league_update'),
    path('player_game/', player_game.list_view, name='player_game_list'),
    path('player_game+<id>/', player_game.detail_view, name='player_game_detail'),
    path('player_game/create/', player_game.create_view, name='player_game_create'),
    path('player_game/update+<id>/', player_game.update_view, name='player_game_update'),
    path('player/', player.list_view, name='player_list'),
    path('player+<id>/', player.detail_view, name='player_detail'),
    path('player/create/', player.create_view, name='player_create'),
    path('player/update+<id>/', player.update_view, name='player_update'),
    path('team/', team.list_view, name='team_list'),
    path('team+<id>/', team.detail_view, name='team_detail'),
    path('team/create/', team.create_view, name='team_create'),
    path('team/update+<id>/', team.update_view, name='team_update'),

]
