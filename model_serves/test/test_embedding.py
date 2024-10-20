from model_serves.config.app_config import ModelConfig
from model_serves.config import rag_config
from model_serves.embedding_model import EmbeddingModel
from model_serves.types import EmbeddingInput
config = ModelConfig(
    embedding_model_name="BAAI/bge-m3",
    llm_api_configs=rag_config.guiji_api_configs,
    )
from model_serves.chat_model import ChatModel
from model_serves.client_manager import ClientManager




if __name__=="__main__": 
    import asyncio

    client_manager = ClientManager(config.llm_api_configs)
  
    from diskcache import Cache
    
    cache = Cache("./caches")
    embedding_model = EmbeddingModel(client_manager, cache)
    
    async def main():
        res = await embedding_model.embedding(model_input=EmbeddingInput(name=config.embedding_model_name, 
                                                                    input_content=[ "你好",  ]
                      ))
        print(res)
    asyncio.run(main())
        