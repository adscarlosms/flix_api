from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie

class MovieModelSerializer(serializers.ModelSerializer):

    #Abaixo, é um campo calculado
    rate = serializers.SerializerMethodField(read_only=True)    
    class Meta:
        model  = Movie
        fields = '__all__'

    #para campo calculado get é obrigatório para buscar o que precisa
    def get_rate(self, obj):
        #a função abaixo simplifica a média sem loops e acessos ao banco
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate,1)
        
        return None

        # reviews = obj.reviews.all()

        # if reviews:
        #     sum_reviews = 0

        #     for review in reviews:
        #         sum_reviews += review.stars

        #     reviews_count = reviews.count()

        #     return round(sum_reviews / reviews_count,1)
    
        # return None

    #função que inicia com validate para validar dados
    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1990')
        return value
    
    def validate_resume(self, value):
        if len(value) >500:
            raise serializers.ValidationError('O campo resumo não pode conter mais de 200 caracteres')
        return value