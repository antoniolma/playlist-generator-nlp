from google import genai
import os
from models import FormatoResposta

client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

class PlaylistGenerator:
    def __init__(self, config, model):
        """
        Playlist generator Agent base on user's input of desired playlist model. \\
        
        """
        # Ultima proposta feita por ESTE agente
        self.last_proposition = ""

        # Config e model for LLM (Gemini)
        self.model_gemini = model
        self.config_gemini = config

    def initialRequest(self, request: str) -> str:
        """
        Initial request for the LLM. \\
        The agent takes the request to Gemini, gets a respose and returns the playlist generated.

        **request**: User's input and request for the LLM.
        """

        prompt = f"""
        Você é um especialista em música e construção de playlists. 
        Você deve analisar o seguinte pedido de playlist e construir uma seleção de músicas que se encaixem no tema solicitado.
        Refira-se EXCLUSIVAMENTE ao pedido fornecido para criar a playlist.
        A playlist deve ser composta por 10 músicas, com o nome da música, do artista e possível featuring.
        A resposta deve ser uma lista em formato JSON, com os seguintes campos:
        - nome_musica: Nome da música
        - artista: Nome do artista
        - featuring: Nome do artista convidado (caso exista)

        Pedido do usuário: {request}
        """

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                'response_schema': list[FormatoResposta],
                'temperature': 1.0
                # 'max_output_tokens': 500,
            }
        )

        self.last_proposition =  f"{response}"

        return response
    
    def refactorPlaylist(self, feedback: str) -> str:
        prompt = f"""
        Dado sua última iteração, foi chamado um outro especialista de músicas para poder te ajudar propondo feedbacks e melhorias.
        Escute atentamente o que for pedido, mas somente faça mudanças que venham de feedbacks que julgar úteis, depois construa uma seleção de músicas que se encaixem no tema solicitado.
        Refira-se EXCLUSIVAMENTE ao pedido fornecido para criar a playlist.
        A playlist deve ser composta por 10 músicas, com o nome da música, do artista e possível featuring.
        A resposta deve ser uma lista em formato JSON, com os seguintes campos:
        - nome_musica: Nome da música
        - artista: Nome do artista
        - featuring: Nome do artista convidado (caso exista)

        Sua última proposta:
        {self.last_proposition}
        
        Feedback do especialista:
        {feedback}
        """
        
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                'response_schema': list[FormatoResposta],
                'temperature': 1.0
                # 'max_output_tokens': 500,
            }
        )

        return response

# =================================================================================

class Validator():
    def __init__(self, request: str, config, model):

        # Request inicial do usuário
        self.request = request

        # Config e model for LLM (Gemini)
        self.config = config
        self.model = model

    def refactorRequest(self, proposed_playlist: str) -> str:

        prompt = f"""
        Você é um especialista em música, com a missão de agir como controle de qualidade de playlists.
        Você receberá o pedido inicial do cliente e a proposta de playlist feita pelo gerador de playlists responsável.
        Pedido do cliente:
        {self.request}

        Proposta de playlist:
        {proposed_playlist}
        
        Faça uma crítica construtiva sobre a playlist recebida, avalia e proponha sugestões de melhorias.
        """

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
            config={
                'temperature': 1.0
            }
        )

        return response
