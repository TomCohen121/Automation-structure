class UsersForMessages:
    users = {
        "profession_user": "https://djmgx4dl196h1.cloudfront.net/dashboard?f5=ZjVTU089ZjVTU091c2VyPTIwMzE0NTQ1MyZmNVNTT3Bhc3N3b3JkPTEyMzQ1Ng0K",
        "second_profession_user": "https://djmgx4dl196h1.cloudfront.net/dashboard?f5=ZjVTU089ZjVTU091c2VyPTAzOTI5MDgwNCZmNVNTT3Bhc3N3b3JkPTEyMzQ1Ng0K",
        "role_user": "https://djmgx4dl196h1.cloudfront.net/dashboard?f5=ZjVTU089ZjVTU091c2VyPTMwODExNTU0MiZmNVNTT3Bhc3N3b3JkPTEyMzQ1Ng0K",
        "second_role_user": "https://djmgx4dl196h1.cloudfront.net/dashboard?f5=ZjVTU089ZjVTU091c2VyPTMwODI4NTUzNSZmNVNTT3Bhc3N3b3JkPTEyMzQ1Ng0K",
        "role_and_profession_user": "https://djmgx4dl196h1.cloudfront.net/dashboard?f5=ZjVTU089ZjVTU091c2VyPTA1NTg5ODg5NCZmNVNTT3Bhc3N3b3JkPTEyMzQ1Ng0K",
        "second_role_and_profession_user": "https://djmgx4dl196h1.cloudfront.net/dashboard?f5=ZjVTU089ZjVTU091c2VyPTA1Njc0NDkzMSZmNVNTT3Bhc3N3b3JkPTEyMzQ1Ng0K",
    }

    @classmethod
    def get_user_url(cls, role):
        return cls.users.get(role)



