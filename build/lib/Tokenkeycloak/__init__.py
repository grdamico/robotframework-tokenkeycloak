from .connection import GetTokenkeycloak


class Tokenkeycloak(object):
    def __init__(self):
        self._keycloaktoken = GetTokenkeycloak()

    def get_keycloak_token(self, host, baseurl, username, password, client_id, grant_type, client_secret, call="POST", contenttype="application/x-www-form-urlencoded"):
        """ With this keyword you can take all info about the token of keycloak

        *Examples*

        | `Get Keycloak Token` | host | baseurl | username | password | client_id | grant_type | client_secret | call="POST" | contenttype="application/x-www-form-urlencoded" |
        
        *All Token*

        | ${ TOKEN } | `Get Keycloak Token` | host | baseurl | username | password | client_id | grant_type | client_secret |
        | Log To Console | ${ TOKEN } |
        
        *Parts of the Token*

        | &{ TOKEN } | `Get Keycloak Token` | host | baseurl | username | password | client_id | grant_type | client_secret |
        | Log To Console | &{ TOKEN } |
        | Log To Console | &{ TOKEN }[access_token] |
        | Log To Console | &{ TOKEN }[expires_in] |
        | Log To Console | &{ TOKEN }[refresh_expires_in] |
        | Log To Console | &{ TOKEN }[refresh_token] |
        | Log To Console | &{ TOKEN }[token_type] |
        | Log To Console | &{ TOKEN }[not_before_policy] |
        | Log To Console | &{ TOKEN }[session_state] |
        | Log To Console | &{ TOKEN }[scope] |
        """
        return self._keycloaktoken.get_token(host, baseurl, username, password, client_id, grant_type, client_secret, call="POST", contenttype="application/x-www-form-urlencoded")