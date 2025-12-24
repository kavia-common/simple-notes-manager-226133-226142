from django.db.models import Q
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Note
from .serializers import NoteSerializer


class StandardResultsSetPagination(PageNumberPagination):
    """
    Standard page-number pagination with configurable page size via query param.
    """
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


# PUBLIC_INTERFACE
@api_view(["GET"])
def health(request: Request) -> Response:
    """Healthcheck endpoint indicating the service is up."""
    return Response({"message": "Server is up!"}, status=status.HTTP_200_OK)


# PUBLIC_INTERFACE
class NoteListCreateView(generics.ListCreateAPIView):
    """
    List notes with pagination, search, and ordering; create new notes.

    Query params:
    - search: performs case-insensitive search on title and content
    - ordering: field to order by (supports 'updated_at' and '-updated_at')
    - page: page number (pagination)
    - page_size: items per page (default 10, max 100)
    """
    serializer_class = NoteSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = Note.objects.all()
        search_query = self.request.query_params.get("search")
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | Q(content__icontains=search_query)
            )
        ordering = self.request.query_params.get("ordering")
        # Only allow safe ordering fields
        allowed = {"updated_at", "-updated_at", "created_at", "-created_at", "title", "-title"}
        if ordering in allowed:
            queryset = queryset.order_by(ordering)
        else:
            queryset = queryset.order_by("-updated_at")
        return queryset


# PUBLIC_INTERFACE
class NoteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a single note by ID.
    """
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
