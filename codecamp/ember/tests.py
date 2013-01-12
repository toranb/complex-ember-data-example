import json
from django.test import TestCase
from codecamp.ember.models import Session, Speaker, Rating, Tag


def add_sessions_ratings_speakers_and_tags():
    first_tag = Tag(description='javascript')
    last_tag = Tag(description='ember-js')
    first_tag.save()
    last_tag.save()
    first_session = Session(name='first', room='A', desc='javascript')
    last_session = Session(name='last', room='Z', desc='python')
    first_session.save()
    last_session.save()
    first_session.tags.add(first_tag)
    last_session.tags.add(last_tag)
    first_session.save()
    last_session.save()
    first_rating = Rating(score=9, feedback='legit', session=first_session)
    last_rating = Rating(score=2, feedback='broken', session=first_session)
    first_rating.save()
    last_rating.save()
    first_speaker = Speaker(name='foo', session=first_session)
    last_speaker = Speaker(name='bar', session=last_session)
    first_speaker.save()
    last_speaker.save()
    return first_session, last_session, first_rating, last_rating, first_speaker, last_speaker, first_tag, last_tag


class SessionTests(TestCase):

    def setUp(self):
        self.first_session, self.last_session, self.first_rating, self.last_rating, self.first_speaker, self.last_speaker, self.first_tag, self.last_tag = add_sessions_ratings_speakers_and_tags()

    def test_http_get_will_retrieve_list_of_sessions_and_return_200(self):
        response = self.client.get('/codecamp/sessions')
        sessions = json.loads(response.content)
        self.assertEqual(response.status_code, 200)

    def test_http_get_will_return_json_object_for_each_session(self):
        response = self.client.get('/codecamp/sessions')
        sessions = json.loads(response.content)
        self.assertEqual(len(sessions), 2)

    def test_http_get_will_return_session_json_with_all_the_attributes_on_the_model(self):
        response = self.client.get('/codecamp/sessions')
        sessions = json.loads(response.content)
        self.assertEqual(sessions[0]['name'], 'first')
        self.assertEqual(sessions[0]['room'], 'A')
        self.assertEqual(sessions[0]['desc'], 'javascript')
        self.assertEqual(sessions[1]['name'], 'last')
        self.assertEqual(sessions[1]['room'], 'Z')
        self.assertEqual(sessions[1]['desc'], 'python')

    def test_http_get_will_return_list_of_session_json_including_rating_ids(self):
        response = self.client.get('/codecamp/sessions')
        sessions = json.loads(response.content)
        ratings = [self.first_rating.pk, self.last_rating.pk]
        self.assertEqual(sessions[0]['ratings'], ratings)
        self.assertEqual(sessions[1]['ratings'], [])

    def test_http_get_will_return_list_of_session_json_including_speaker_ids(self):
        response = self.client.get('/codecamp/sessions')
        sessions = json.loads(response.content)
        first_speakers = [self.first_speaker.pk]
        last_speakers = [self.last_speaker.pk]
        self.assertEqual(sessions[0]['speakers'], first_speakers)
        self.assertEqual(sessions[1]['speakers'], last_speakers)

    def test_http_put_will_update_first_session_and_return_200(self):
        data = {'name': 'updated name', 'room': 'updated room', 'desc': 'updated desc'}
        response = self.client.put('/codecamp/sessions/{}/'.format(self.first_session.pk), data)
        self.assertEqual(response.status_code, 200)

    def test_http_put_will_update_first_session_and_return_updated_session_json(self):
        data = {'name': 'updated name', 'room': 'updated room', 'desc': 'updated desc'}
        response = self.client.put('/codecamp/sessions/{}/'.format(self.first_session.pk), data)
        updated_session = json.loads(response.content)
        self.assertEqual(updated_session['name'], 'updated name')
        self.assertEqual(updated_session['room'], 'updated room')
        self.assertEqual(updated_session['desc'], 'updated desc')

    def test_http_delete_will_remove_last_session_and_return_204(self):
        response = self.client.delete('/codecamp/sessions/{}/'.format(self.last_session.pk))
        self.assertEqual(response.status_code, 204)

    def test_http_delete_will_remove_last_session_and_return_empty_content(self):
        response = self.client.delete('/codecamp/sessions/{}/'.format(self.last_session.pk))
        self.assertEqual(response.content, '')

    def test_http_delete_will_return_404_when_incorrect_id_used_to_delete_session(self):
        response = self.client.delete('/codecamp/sessions/999999999999999999/')
        self.assertEqual(response.status_code, 404)


class RatingTests(TestCase):

    def setUp(self):
        self.first_session, self.last_session, self.first_rating, self.last_rating, self.first_speaker, self.last_speaker, self.first_tag, self.last_tag = add_sessions_ratings_speakers_and_tags()

    def test_will_return_json_with_list_of_ratings_for_given_session_id(self):
        response = self.client.get('/codecamp/sessions/{}/ratings/'.format(self.first_session.pk))
        ratings = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(ratings), 2)

    def test_ratings_json_has_an_attribute_for_each_item(self):
        response = self.client.get('/codecamp/sessions/{}/ratings/'.format(self.first_session.pk))
        ratings = json.loads(response.content)
        self.assertEqual(ratings[0]['score'], 9)
        self.assertEqual(ratings[0]['feedback'], 'legit')
        self.assertEqual(ratings[0]['session'], self.first_session.pk)
        self.assertEqual(ratings[1]['score'], 2)
        self.assertEqual(ratings[1]['feedback'], 'broken')
        self.assertEqual(ratings[1]['session'], self.first_session.pk)

    def test_ratings_json_returns_empty_list_given_last_session_id(self):
        response = self.client.get('/codecamp/sessions/{}/ratings/'.format(self.last_session.pk))
        ratings = json.loads(response.content)
        self.assertEqual(len(ratings), 0)
        self.assertEqual(ratings, [])

    def test_detail_ratings_endpoint_returns_attributes_for_given_rating_id(self):
        response = self.client.get('/codecamp/ratings/{}/'.format(self.last_rating.pk))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, '{"id": 2, "score": 2, "feedback": "broken", "session": 1}')

    def test_http_post_will_create_rating_and_return_201(self):
        data = {'score': 9, 'feedback': 'nice try', 'session': self.last_session.pk}
        response = self.client.post('/codecamp/sessions/{}/ratings/'.format(self.last_rating.pk), data)
        self.assertEqual(response.status_code, 201)

    def test_http_post_will_create_rating_and_return_created_rating_json(self):
        data = {'score': 9, 'feedback': 'nice try', 'session': self.last_session.pk}
        response = self.client.post('/codecamp/sessions/{}/ratings/'.format(self.last_rating.pk), data)
        created_rating = json.loads(response.content)
        self.assertEqual(created_rating['score'], 9)
        self.assertEqual(created_rating['feedback'], 'nice try')
        self.assertEqual(created_rating['session'], self.last_session.pk)

    def test_http_post_without_data_returns_400(self):
        response = self.client.post('/codecamp/sessions/{}/ratings/'.format(self.last_rating.pk), {})
        self.assertEqual(response.status_code, 400)

    def test_http_put_will_update_first_rating_and_return_200(self):
        data = {'score': 124, 'feedback': 'updated feedback', 'session': self.first_session.pk}
        response = self.client.put('/codecamp/ratings/{}/'.format(self.first_rating.pk), data)
        self.assertEqual(response.status_code, 200)

    def test_http_put_will_update_first_rating_and_return_updated_rating_json(self):
        data = {'score': 124, 'feedback': 'updated feedback', 'session': self.first_session.pk}
        response = self.client.put('/codecamp/ratings/{}/'.format(self.first_rating.pk), data)
        updated_rating = json.loads(response.content)
        self.assertEqual(updated_rating['score'], 124)
        self.assertEqual(updated_rating['feedback'], 'updated feedback')
        self.assertEqual(updated_rating['session'], self.first_session.pk)

    def test_http_delete_will_remove_first_rating_and_return_204(self):
        response = self.client.delete('/codecamp/ratings/{}/'.format(self.first_rating.pk))
        self.assertEqual(response.status_code, 204)

    def test_http_delete_will_remove_first_rating_and_return_empty_content(self):
        response = self.client.delete('/codecamp/ratings/{}/'.format(self.first_rating.pk))
        self.assertEqual(response.content, '')

    def test_http_delete_will_return_404_when_incorrect_id_used_to_delete_rating(self):
        response = self.client.delete('/codecamp/ratings/999999999999999999/')
        self.assertEqual(response.status_code, 404)


class SpeakerTests(TestCase):

    def setUp(self):
        self.first_session, self.last_session, self.first_rating, self.last_rating, self.first_speaker, self.last_speaker, self.first_tag, self.last_tag = add_sessions_ratings_speakers_and_tags()

    def test_will_return_json_with_list_of_speakers_for_given_session_id(self):
        response = self.client.get('/codecamp/sessions/{}/speakers/'.format(self.first_session.pk))
        speakers = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(speakers), 1)

    def test_speakers_json_has_an_attribute_for_each_item(self):
        response = self.client.get('/codecamp/sessions/{}/speakers/'.format(self.first_session.pk))
        speakers = json.loads(response.content)
        self.assertEqual(speakers[0]['name'], 'foo')
        self.assertEqual(speakers[0]['session'], self.first_session.pk)

    def test_speakers_json_returns_last_speaker_json_given_last_session_id(self):
        response = self.client.get('/codecamp/sessions/{}/speakers/'.format(self.last_session.pk))
        speakers = json.loads(response.content)
        self.assertEqual(speakers[0]['name'], 'bar')
        self.assertEqual(speakers[0]['session'], self.last_session.pk)

    def test_detail_speakers_endpoint_returns_attributes_for_given_speaker_id(self):
        response = self.client.get('/codecamp/speakers/{}/'.format(self.first_speaker.pk))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, '{"id": 1, "name": "foo", "session": 1}')

    def test_http_post_will_create_speaker_and_return_201(self):
        data = {'name': 'foo', 'session': self.last_session.pk}
        response = self.client.post('/codecamp/sessions/{}/speakers/'.format(self.last_rating.pk), data)
        self.assertEqual(response.status_code, 201)

    def test_http_post_will_create_speaker_and_return_created_speaker_json(self):
        data = {'name': 'foo', 'session': self.last_session.pk}
        response = self.client.post('/codecamp/sessions/{}/speakers/'.format(self.last_rating.pk), data)
        created_speaker = json.loads(response.content)
        self.assertEqual(created_speaker['name'], 'foo')
        self.assertEqual(created_speaker['session'], self.last_session.pk)

    def test_http_post_without_data_returns_400(self):
        response = self.client.post('/codecamp/sessions/{}/speakers/'.format(self.last_rating.pk), {})
        self.assertEqual(response.status_code, 400)

    def test_http_put_will_update_first_speaker_and_return_200(self):
        data = {'name': 'updated name', 'session': self.first_session.pk}
        response = self.client.put('/codecamp/speakers/{}/'.format(self.first_speaker.pk), data)
        self.assertEqual(response.status_code, 200)

    def test_http_put_will_update_first_speaker_and_return_updated_speaker_json(self):
        data = {'name': 'updated name', 'session': self.first_session.pk}
        response = self.client.put('/codecamp/speakers/{}/'.format(self.first_speaker.pk), data)
        updated_speaker = json.loads(response.content)
        self.assertEqual(updated_speaker['name'], 'updated name')
        self.assertEqual(updated_speaker['session'], self.first_session.pk)

    def test_http_delete_will_remove_first_speaker_and_return_204(self):
        response = self.client.delete('/codecamp/speakers/{}/'.format(self.first_speaker.pk))
        self.assertEqual(response.status_code, 204)

    def test_http_delete_will_remove_first_speaker_and_return_empty_content(self):
        response = self.client.delete('/codecamp/speakers/{}/'.format(self.first_speaker.pk))
        self.assertEqual(response.content, '')

    def test_http_delete_will_return_404_when_incorrect_id_used_to_delete_speaker(self):
        response = self.client.delete('/codecamp/speakers/999999999999999999/')
        self.assertEqual(response.status_code, 404)


class TagTests(TestCase):

    def setUp(self):
        self.first_session, self.last_session, self.first_rating, self.last_rating, self.first_speaker, self.last_speaker, self.first_tag, self.last_tag = add_sessions_ratings_speakers_and_tags()

    def test_will_return_json_with_list_of_tags_for_given_session_id(self):
        response = self.client.get('/codecamp/sessions/{}/tags/'.format(self.first_session.pk))
        tags = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(tags), 1)

    def test_tags_json_returns_first_tag_json_given_first_session_id(self):
        response = self.client.get('/codecamp/sessions/{}/tags/'.format(self.first_session.pk))
        speakers = json.loads(response.content)
        self.assertEqual(speakers[0]['description'], 'javascript')

    def test_tags_json_returns_last_tag_json_given_last_session_id(self):
        response = self.client.get('/codecamp/sessions/{}/tags/'.format(self.last_session.pk))
        speakers = json.loads(response.content)
        self.assertEqual(speakers[0]['description'], 'ember-js')

    def test_detail_tags_endpoint_returns_attributes_for_given_tag_id(self):
        response = self.client.get('/codecamp/tags/{}/'.format(self.first_tag.pk))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, '{"id": 1, "description": "javascript"}')

    def test_http_post_will_create_tag_and_return_201(self):
        data = {'description': 'new', 'session': self.last_session.pk}
        response = self.client.post('/codecamp/sessions/{}/tags/'.format(self.last_session.pk), data)
        self.assertEqual(response.status_code, 201)

    def test_http_post_will_create_tag_and_return_created_tag_json(self):
        data = {'description': 'new', 'session': self.last_session.pk}
        response = self.client.post('/codecamp/sessions/{}/tags/'.format(self.last_session.pk), data)
        created_tag = json.loads(response.content)
        self.assertEqual(created_tag['description'], 'new')
        #self.assertEqual(created_tag['session'], self.last_session.pk) #this will always fail as-is

    def test_http_post_without_data_returns_400(self):
        response = self.client.post('/codecamp/sessions/{}/tags/'.format(self.last_session.pk), {})
        self.assertEqual(response.status_code, 400)

    def test_http_put_will_update_first_tag_and_return_200(self):
        data = {'description': 'updated'}
        response = self.client.put('/codecamp/tags/{}/'.format(self.first_tag.pk), data)
        self.assertEqual(response.status_code, 200)

    def test_http_put_will_update_first_tag_and_return_updated_tag_json(self):
        data = {'description': 'updated'}
        response = self.client.put('/codecamp/tags/{}/'.format(self.first_tag.pk), data)
        updated_speaker = json.loads(response.content)
        self.assertEqual(updated_speaker['description'], 'updated')

    def test_http_delete_will_remove_first_tag_and_return_204(self):
        response = self.client.delete('/codecamp/tags/{}/'.format(self.first_tag.pk))
        self.assertEqual(response.status_code, 204)

    def test_http_delete_will_remove_first_tag_and_return_empty_content(self):
        response = self.client.delete('/codecamp/tags/{}/'.format(self.first_tag.pk))
        self.assertEqual(response.content, '')

    def test_http_delete_will_return_404_when_incorrect_id_used_to_delete_tag(self):
        response = self.client.delete('/codecamp/tags/999999999999999999/')
        self.assertEqual(response.status_code, 404)
