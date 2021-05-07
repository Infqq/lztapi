import requests


class Lzt:
        def __init__(
                self, api_token = ""
                ):

                s = requests.Session()
                s.headers = {'Authorization': f'Bearer {api_token}','Cookie': 'xf_logged_in=1'}
                
                self._s = s

        def userfind(
                self, username="", user_email=""):
                
                r = self._s.get(url=f"https://lolz.guru/api/index.php?users/find&username={username}&user_email={user_email}").json()
                return r
        
        def threads(
                self, forum_id="", thread_ids="", creator_user_id="", sticky="", thread_prefix_id="",
                thread_tag_id="", page="", limit="", order="", thread_create_date="", thread_update_date=""):
                
                r = self._s.get(url=f"https://lolz.guru/api/index.php?threads/&forum_id={forum_id}&thread_ids={thread_ids}&creator_user_id={creator_user_id}&sticky={sticky}&thread_prefix_id={thread_prefix_id}&thread_tag_id={thread_tag_id}&page={page}&limit={limit}&order={order}&thread_create_date={thread_create_date}&thread_update_date={thread_update_date}").json()
                return r
        
        def profilePosts(
                self, userid, page="", limit=""):
                
                r = self._s.get(url=f"https://lolz.guru/api/index.php?users/{userid}/timeline&page={page}&limit={limit}").json()
                return r
        
        def posts(
                self, thread_id, page_of_post_id="", post_ids="", page="", limit="", order=""):
                
                r = self._s.get(url=f"https://lolz.guru/api/index.php?posts/&thread_id={thread_id}&page_of_post_id={page_of_post_id}&post_ids={post_ids}&page={page}&limit={limit}&order={order}").json()
                return r
        
        def conversations(
                self, page="", limit=""):
                
                r = self._s.get(url=f"https://lolz.guru/api/index.php?conversations/&page={page}&limit={limit}").json()
                return r
        
        def threadInfo(
                self, page="", limit=""):
                
                r = self._s.get(url=f"https://lolz.guru/api/index.php?threads/{page}").json()
                return r
        
        def conversation(
                self, conversation_id, page="", limit="", order="", before="", after=""):
                
                r = self._s.get(url=f"https://lolz.guru/api/index.php?conversation-messages/&conversation_id={conversation_id}&limit={limit}&page={page}&order={order}&before={before}&after={after}").json()
                return r
        
        def notifications(self):
                r = self._s.get(url=f"https://lolz.guru/api/index.php?notifications").json()
                return r

        def pages(
                self, parent_page_id="", order=""):
                
                r = self._s.get(url=f"https://lolz.guru/api/index.php?pages").json()
                return r
        
        def pagesById(
                self, page_id):
                
                r = self._s.get(url=f"https://lolz.guru/api/index.php?pages/{page_id}").json()

                return r
        def new_post(
                self, thread_id, post_text, quote_post_id=""):
                
                r = s.post(url=f"https://lolz.guru/api/index.php?posts/&thread_id={thread_id}&post_body={post_text}&quote_post_id={quote_post_id}").json()
                return r
