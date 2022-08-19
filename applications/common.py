from rest_framework import viewsets


class MultiSerializerViewSet(viewsets.ModelViewSet):
    """
    Model Viewset Mixin that accepts multiple serializers.
    """
    
    serializers = { 
        'default': None,
    }

    def get_serializer_class(self):
        """
        Returns default serializer for viewset class.
        """

        return self.serializers.get(
            self.action,self.serializers['default'])

    def map_serialized_item_to_list(self, object, objects_list):
        """
        Applies one object to a list of objects.
        """

        return [{**object, **item} for item in objects_list]

