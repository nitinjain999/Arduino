from temboo.Library.Dropbox.OAuth import InitializeOAuth
from temboo.core.session import TembooSession

# Create a session with your Temboo account details
session = TembooSession("accountName", "myFirstApp", "abc123xxxxxxxxxxxxxx")

# Instantiate the Choreo
initializeOAuthChoreo = InitializeOAuth(session)

# Get an InputSet object for the Choreo
initializeOAuthInputs = initializeOAuthChoreo.new_input_set()

# Set credential to use for execution
initializeOAuthInputs.set_credential('enjnjnj')

# Execute the Choreo
initializeOAuthResults = initializeOAuthChoreo.execute_with_results(initializeOAuthInputs)

# Print the Choreo outputs
print("AuthorizationURL: " + initializeOAuthResults.get_AuthorizationURL())
print("CallbackID: " + initializeOAuthResults.get_CallbackID())
print("OAuthTokenSecret: " + initializeOAuthResults.get_OAuthTokenSecret())