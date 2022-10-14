# Developing Multi-agent systems using SPADE

Smart Python Agent Development Environment is an open source python library, made to create multi-agent systems using the eXtensible Messaging and Presence Protocol (XMPP).

SPADE makes developing agents that chat with each other really easy to manage and control, and is very easy to implement into an API that you can use for various projects. In this tutorial, we will show you how to install setup and create a MAS with all the features that SPADE provides.

## Installation :

All you need to do is open your terminal and type this command`

```bash
$ pip install spade
```

you will then need to install an XMPP server that you can find on this link :

https://xmpp.org/getting-started/

(I personally recommend installing Gajim)

Once you are done, all you need to do is to create an XMPP account for your agent and you can start coding.

## Create a Multi-agent system :

First you need to do the different imports :

```python
from spade.agent import Agent
from spade.behaviour import FSMBehaviour, State
from spade.message import Message
```

Then all we need to do is create an agent class with the appropriate behaviours



```python
class Your_Agents(Agent):
        class behavior(FSMBehaviour):
                async def on_start(self):
                        pass
                async def on_end(self):
                        pass
       # This function is the one that takes care of send a msg to another
       # agent
        class sending(State):
                async def run(self):
                        agents=[
                                    #list of agents you want to send them the msg
                               ]
                        for agent in agents:
                            msg = Message(to=agent)
                            msg.set_metadata("performative", "inform")  # Set the "inform" FIPA performative
                            msg.body = "Your Message"
                            await self.send(msg)
                        self.set_next_state("waiting")
        # This function is the one that takes care of receiving a msg 
        # from another agent
        class waiting(State):
                async def run(self):
                        msg = await self.receive(timeout=10)
                        if msg:
                                # Do what you want with the message in 
                                # our case we will just print it
                                print(msg)
                                await self.agent.stop()

        # this function is the one that will setup your agent     
        async def setup(self):
                fsm = self.behavior()
                fsm.add_state(name="sending", state = self.sending(), initial = True)
                fsm.add_state(name="waiting", state = self.waiting())

                fsm.add_transition(source = "sending", dest = "waiting")
                fsm.add_transition(source = "waiting", dest = "sending")

                self.add_behaviour(fsm)

        # After this you can add any function you like depending on the 
        # behaviours of your agent 
```

You can create as many agent as you want each one of them can have his own tasks then all you need to do is to invoke them :

```python
agent1 = ma.Your_Agents("your_jid@your_xmpp_server", "your_password")
agent1.start() # launch your agent
agent1.task1() # a function that you created yourself which does a specific behaviour


agent2 = ma.Another_Agents("your_jid@your_xmpp_server", "your_password")
futur = agent2.start() # launch your agent
agent2.another_task()
futur.result() # to receive the result of the msg


agent1.stop()
agent2.stop()
```

And like this we created a simple MAS template with all the basic behaviour that can be used. Having differents agents performing different tasks and communicating between each others is a very powerful tool that help to solve very complex problems and be used in various cases.

If you want to learn more about SPADE you can check the official documentation here [SPADE documentation](https://spade-mas.readthedocs.io/en/latest/readme.html)


