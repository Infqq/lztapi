import requests


class lztapi:
        def __init__(
                self, api_token
                ) -> str:
                
                self._api_token = api_token

        def user_find(
                self, username="", user_email=""):
                
                response = requests.get(url=f"https://lolz.guru/api/index.php?users/find&username={username}&user_email={user_email}").json()
                return response
        
        def threads(
                self, forum_id="", thread_ids="", creator_user_id="", sticky="", thread_prefix_id="",
                thread_tag_id="", page="", limit="", order="", thread_create_date="", thread_update_date=""):
                
                response = requests.get(url=f"https://lolz.guru/api/index.php?threads/&forum_id={forum_id}&thread_ids={thread_ids}&creator_user_id={creator_user_id}&sticky={sticky}&thread_prefix_id={thread_prefix_id}&thread_tag_id={thread_tag_id}&page={page}&limit={limit}&order={order}&thread_create_date={thread_create_date}&thread_update_date={thread_update_date}&oauth_token={self._api_token}").json()
                return response
        
        def profilePosts(
                self, userid, page="", limit=""):
                
                response = requests.get(url=f"https://lolz.guru/api/index.php?users/{userid}/timeline&page={page}&limit={limit}").json()
                return response
        
        def posts(
                self, thread_id, page_of_post_id="", post_ids="", page="", limit="", order=""):
                
                response = requests.get(url=f"https://lolz.guru/api/index.php?posts/&thread_id={thread_id}&page_of_post_id={page_of_post_id}&post_ids={post_ids}&page={page}&limit={limit}&order={order}&oauth_token={self._api_token}").json()
                return response
