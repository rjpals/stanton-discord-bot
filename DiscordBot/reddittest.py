import praw, random, itertools


def main():
    print("--------------------")
    print("asdf " + random_hot_post())
    print("--------------------")


def random_hot_post(subreddit):
    r = praw.Reddit(user_agent='Test Script by /u/ryanjpals')
    submissions = r.get_subreddit(subreddit).get_hot(limit=25)

    num = random.randrange(1, 25) - 1

    hot_page = list(itertools.islice(submissions, 25))

    random_page = hot_page[num]

    if subreddit != 'shitpost':
        return random_page.url

    linked_post = r.get_submission(url=random_page.url)
    return linked_post.url

if __name__ == "__main__":
    main()