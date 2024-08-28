from abc import ABC, abstractmethod

class Middleware(ABC):
    """
    Abstract base class for creating middleware in the Storm framework.
    """
    @abstractmethod
    async def process_request(self, request, next_handler):
        """
        Processes the request before it reaches the handler.

        :param request: The incoming HTTP request
        :param next_handler: The next middleware or handler in the pipeline
        :return: The result of the next handler
        """
        pass

    @abstractmethod
    async def process_response(self, response):
        """
        Processes the response before it is sent to the client.

        :param response: The response generated by the handler
        :return: The processed response
        """
        pass
