def create_youtube_video(title, description):
	youtube_video = {"title":title, "description":description, "likes":0, "dislikes":0, "comments":{}}
	return youtube_video

def like(youtube_video):
	if "likes" in youtube_video:
		youtube_video["likes"] += 1

def dislike(youtube_video):
	if "dislikes" in youtube_video:
		youtube_video["dislikes"] += 1

def add_comment(youtubevideo, username, comment_text):
	youtubevideo['comments'] = {username, comment_text}
	return youtubevideo


def main():
	new_youtube_dict = create_youtube_video("meet 2022", "Summer")
	like(new_youtube_dict)
	dislike(new_youtube_dict)
	add_comment(new_youtube_dict, "niv", "I liked your video")
	print("Title: ", new_youtube_dict['title'])
	print("Description: ", new_youtube_dict['description'])
	print(new_youtube_dict['likes'], " people liked this :)")
	print(new_youtube_dict['dislikes'], " people disliked this :(")
	print("Comments: \n==========")
	print(new_youtube_dict['comments'])

if __name__ == '__main__':
	main()
