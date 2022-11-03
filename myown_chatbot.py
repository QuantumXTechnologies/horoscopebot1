import os
import requests
from rasa_core.channels.rasa_chat import RasaChatInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig

# load your trained agent
interpreter = RasaNLUInterpreter("models/nlu/default/horoscopebot/")
MODEL_PATH = "models/dialogue"
action_endpoint = EndpointConfig(url="https://horoscopebot1.herokuapp.com/webhook")

agent = Agent.load(MODEL_PATH, interpreter=interpreter, action_endpoint=action_endpoint )


class MyNewInput(RasaChatInput):
    def _check_token(self, token):
        if token == 'mysecret':
            return {'username': 1234}
        else:
            print("Failed to check token: {}.".format(token))
            return None


input_channel = MyNewInput(url='https://horoscopebot1.herokuapp.com')
# set serve_forever=False if you want to keep the server running
s = agent.handle_channels([input_channel], int(os.environ.get('PORT', 5004)), serve_forever=True)


def _check_token(self, token):
    url = "{}/users/me".format(self.base_url)
    headers = {"Authorization": token}
    logger.debug("Requesting user information from auth server {}."
                 "".format(url))
    result = requests.get(url,
                          headers=headers,
                          timeout=DEFAULT_REQUEST_TIMEOUT)
    if result.status_code == 200:
        return result.json()
    else:
        logger.info("Failed to check token: {}. "
                    "Content: {}".format(token, request.data))
        return None
