import time
import numpy as np
from gym.spaces import Discrete

from comaze.agents.utils import DictObsDiscreteActionExpExtractorClass

class DictObsDiscreteActionSecretRuleExpExtractorClass(DictObsDiscreteActionExpExtractorClass):
  def __init__(self, vocab_size=10, maximum_sentence_length=1, options={}):
    DictObsDiscreteActionExpExtractorClass.__init__(
      self=self,
      vocab_size=vocab_size,
      maximum_sentence_length=maximum_sentence_length,
      options=options
    )

    # Observation Space:
    ## secret_rule : 
    self.secretgoalEnum2id = {"RED":0, "BLUE":1, "GREEN":2, "YELLOW":3}
    ##

  def _get_secret_rule(self, game):
    secret_rule_binary = np.zeros(8)
    
    secret_rule = game["currentPlayer"].get("secretGoalRule", None)

    if secret_rule is not None:
      earlier_goal_id = self.secretgoalEnum2id[secret_rule["earlierGoal"]["color"]]
      later_goal_id = self.secretgoalEnum2id[secret_rule["laterGoal"]["color"]]

      secret_rule_binary[earlier_goal_id] = 1
      secret_rule_binary[4+later_goal_id] = 1
      
    return secret_rule_binary

  def extract_exp(self, game, player):
    obs = {}
    obs["encoded_pov"] = self._encode_game(game=game)
    
    obs["available_actions"] = self._get_available_actions(game=game)
    
    obs["previous_message"] = self._get_previous_message(game=game)
    
    obs["secret_rule"] = self._get_secret_rule(game=game)
    
    return obs 
    
DictObsDiscreteActionSecretRuleExpExtractor = DictObsDiscreteActionSecretRuleExpExtractorClass()
def dict_obs_discrete_action_secret_rule_extract_exp_fn(game, player):
  """
  Provided a game state and player information, 
  this function extracts an experience tuple, i.e.
  (observation, reward, done, infos) in a typical RL fashion.
  """
  global DictObsDiscreteActionSecretRuleExpExtractor
  return DictObsDiscreteActionSecretRuleExpExtractor.extract_exp(game, player)

