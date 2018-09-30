import GitHubApi, unittest
from unittest import mock
from unittest.mock import MagicMock

class Test(unittest.TestCase):
    def test0_repos(self):
        self.assertEqual(GitHubApi.get_repo(''), "Please provide a username")
        user = 0
        self.assertEqual(GitHubApi.get_repo(user), "The input " + str(user) +" is not valid")
        self.assertEqual(GitHubApi.get_repo([]), "A list of repos was not provided")

    @mock.patch('GitHubApi.get_repo')
    def test1_repos(self, mockedReq):
        mockedReq.return_value = ['helloworld']
        repos = GitHubApi.get_repo('richkempinski')
        self.assertIn('helloworld', repos)
        
    @mock.patch('GitHubApi.get_repo')
    def test2_repos(self, mockedReq):
        mockedReq.return_value = ['Triangle567', 'GitHubApi567']
        repo_list = GitHubApi.get_repo('otavara')
        self.assertIn('Triangle567', repo_list)
        self.assertIn('GitHubApi567', repo_list)

    def test0_num_commits(self):
        self.assertEqual(GitHubApi.get_num_commits("otavara",'',''), "A list of repos was not provided")
        self.assertEqual(GitHubApi.get_num_commits("otavara",["Triangle567","GitHubApi567"],''), "Please provide a repo to view")
        self.assertEqual(GitHubApi.get_num_commits("",["Triangle567","GitHubApi567"],'Triangle567'), "Please provide a username")
  
    @mock.patch('GitHubApi.get_num_commits')
    def test1_commits(self, mockedReq):
        repos = GitHubApi.get_repo('richkempinski')
        mockedReq.return_value = 2
        self.assertEqual(GitHubApi.get_num_commits("richkempinski",repos,'helloworld'), 2)

    @mock.patch('GitHubApi.get_num_commits')
    def test2_get_num_commits(self, mockedReq):
        mockedReq.side_effect = [5, 6]
        repos = GitHubApi.get_repo('otavara')
        mockedReq.return_value = MagicMock(5)
        self.assertEqual(GitHubApi.get_num_commits("otavara",repos,'GitHubApi567'), 5)
        mockedReq.return_value = MagicMock(6)
        self.assertEqual(GitHubApi.get_num_commits("otavara",repos,'Triangle567'), 6)

if __name__ == '__main__':
    print('------------ Running Unit Tests ------------')
    unittest.main()