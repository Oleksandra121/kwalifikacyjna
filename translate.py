import torch
from onmt.translate import TranslationServer, ServerModelError

def setup_server(model_path):
    config = {
        "models": [{
            "id": 1000,
            "model": model_path,
            "timeout": 600,
            "on_timeout": "to_cpu",
            "load": True,
            "opt": {
                "gpu": -1,
                "beam_size": 5
            }
        }]
    }
    
    server = TranslationServer()
    server.start(config)  
    return server

def translate_text(server, text):
    try:
        translation = server.run([{
            "id": 1000,
            "src": text,
            "opts": {}
        }])
        return translation[0][0]['tgt']
    except ServerModelError as e:
        return str(e)

def main():
    model_path = "C:/Users/Saszka/kwalifikacyjna//model.pt"  
    server = setup_server(model_path)
    
    source_text = input("Enter text to translate: ")
    translation = translate_text(server, source_text)
    print("Translated text:", translation)

if __name__ == "__main__":
    main()