from rest_framework import serializers
from .models import SavedComic, Image, Character, Story


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['path', 'extension']


class CharacterSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['name', 'role']


class StorySummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['name', 'story_type']


class SavedComicSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    characters = CharacterSummarySerializer(many=True)
    stories = StorySummarySerializer(many=True)

    class Meta:
        model = SavedComic
        fields = ['id', 'user', 'comic_id', 'title', 'description', 'release_date', 'images', 'characters', 'stories']

    def create(self, validated_data):
        images = validated_data.pop('images')
        characters = validated_data.pop('characters')
        stories = validated_data.pop('stories')
        comic = SavedComic.objects.create(**validated_data)

        for image in images:
            image = Image.objects.create(**image)
            comic.images.add(image)

        for character in characters:
            character = Character.objects.create(**character)
            comic.characters.add(character)

        for story in stories:
            story = Story.objects.create(**story)
            comic.stories.add(story)

        return comic
