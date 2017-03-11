import time
from os import path
import vk_api
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def main():
    login, password = 'python@vk.com', 'mypassword'
    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.authorization()
    except vk_api.AuthorizationError as error_msg:
        print(error_msg)
        return

    tools = vk_api.VkTools(vk_session)
    start_time = time.time()
    wall = tools.get_all_iter('messages.getHistory', 200, {'user_id': 1})  # идентификатор пользователя
    # wall = tools.get_all_iter('messages.getHistory', 200, {'peer_id': 2000000001})  # для беседы

    wall = list(wall)
    with open('messages.txt', 'w') as f:
        list(map(lambda i: f.write(i['body'] + " \n"), wall))

    d = path.dirname(__file__)
    text = open(path.join(d, 'messages.txt')).read()
    wordcloud = WordCloud(max_words=300, width=1920, height=1080).generate(text)
    print("--- %s time ---" % (time.time() - start_time))
    plt.imshow(wordcloud)
    plt.axis("off")
    manager = plt.get_current_fig_manager()
    manager.resize(*manager.window.maxsize())
    plt.show()


if __name__ == '__main__':
    main()
