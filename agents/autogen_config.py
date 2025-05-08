from autogen import AssistantAgent, GroupChat, GroupChatManager

def create_agents():
    legal_agent = AssistantAgent(
        name="Legal_Expert",
        system_message="Specialist in regulatory compliance and risk management"
    )
    
    financial_agent = AssistantAgent(
        name="Financial_Analyst",
        system_message = "Expert in cost analysis and funding strategies"
    )
    
    groupchat = GroupChat(
        agents=[legal_agent, financial_agent],
        messages=[],
        max_round=20
    )
    
    return GroupChatManager(groupchat=groupchat)