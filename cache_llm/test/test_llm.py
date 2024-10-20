from cache_llm.config.app_config import ModelConfig
from cache_llm.config import rag_config
from cache_llm.types import LLMInput, Message
config = ModelConfig(
    model_name="glm-4-flash",
    llm_api_configs=rag_config.zhipu_api_configs,
    )
from cache_llm.chat_model import ChatModel
from cache_llm.client_manager import ClientManager




if __name__=="__main__": 
    import asyncio

    client_manager = ClientManager(config.llm_api_configs)
  
    from diskcache import Cache
    
    cache = Cache("./caches")
    
    chat_model = ChatModel(client_manager, cache)
    async def main():
        res = await chat_model.chat(model_input=LLMInput(name=config.model_name, 
                                                                    input_content=[
                                                                        Message(role="user", content="what is your name!"), 
                                                                        ]
                                                      )
                      )
        print(res)
    asyncio.run(main())
        