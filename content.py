import utils

class Content:  # TODO try and consolidate into one single content class!!!
    # TODO add program_ID to __init__

    def __init__(self,
                 content_name,
                 episode_title,
                 content_type,
                 content_description,
                 content_rating,
                 genres,
                 language,
                 channel_name,
                 channel_number,
                 tribune_ID,
                 time_string,
                 cast,
                 qualifiers):
        self.name = content_name
        self.type = content_type
        self.episode_title = episode_title
        self.description = content_description
        self.rating = content_rating
        self.genres = genres
        self.language = language
        self.channel = [channel_name, channel_number]
        self.channel_name = channel_name
        self.channel_number = channel_number
        self.tribune_ID = tribune_ID
        datetime_obj = utils.parseSearchTime(time_string)
        self.duration = datetime_obj[1]
        self.start = utils.adjustTimeFromGMT(datetime_obj[0]) # TODO should be datetime object
        self.end = utils.addSeconds(self.start, int(self.duration)) # TODO should be datetime object
        self.cast = cast
        self.qualifiers = qualifiers

class VideoOnDemand:

    def __init__(self,
                 args):
        # do stuff here
        pass

class RecordedContent:
    def __init__(self,
                 title,
                 description,
                 genres,
                 end_time,
                 tv_rating,
                 sub_rating,
                 mpaa_rating,
                 critic_rating,
                 release_date,
                 callsign,
                 channel_number,
                 start_time,
                 tribune_id,
                 episode_title,
                 episode_number,
                 season_number,
                 qualifiers,
                 cast):
        pass

class ScheduledContent:

    def __init__(self,
                 title,
                 description,
                 genres,
                 end_time,
                 tv_rating,
                 sub_rating,
                 MPAA_rating,
                 critic_rating,
                 release_date,
                 callsign,
                 channel_number,
                 start_time,
                 tribune_ID,
                 episode_title,
                 episode_number,
                 season_number,
                 qualifiers,
                 cast):

        self.title = title
        self.description = description
        self.genres = genres.split(",")
        self.end_time = utils.genDatetimeObjFromScheduled(end_time)
        self.ratings = {}
        self.ratings["TV"] = tv_rating
        self.ratings["Sub"] = sub_rating
        self.ratings["MPAA"] = MPAA_rating
        self.ratings["Critic"] = critic_rating
        self.release_date = utils.genDatetimeObjFromReleaseDate(release_date)
        self.callsign = callsign
        self.channel_number = channel_number
        self.start_time = utils.genDatetimeObjFromScheduled(start_time)
        self.tribune_ID = tribune_ID
        self.episode_title = episode_title
        self.episode_number = episode_number
        self.season_number = season_number
        self.qualifiers = qualifiers
        if cast:
            self.cast = cast.split(",")
        else:
            self.cast = cast

class BestBet:

    def __init__(self,
                 positive_content,
                 program_title,
                 program_id,
                 program_service_id,
                 program_service_name,
                 event_id,
                 air_date_time,
                 duration,
                 language,
                 channel_number,
                 program_type,
                 tv_rating,
                 mpaa_rating,
                 callsign,
                 media_caption=None):
        self.positive_content = positive_content
        self.title = program_title
        self.program_ID = program_id
        self.provider_ID = program_service_id
        self.provider_name = program_service_name
        self.event_ID = event_id
        self.air_date_time = air_date_time
        self.duration = duration
        self.end = False
        self.language = language
        self.channel_number = channel_number
        self.type = program_type
        self.ratings = {}
        self.ratings["TV"] = tv_rating
        self.ratings["MPAA"] = mpaa_rating
        self.callsign = callsign
        self.media_caption = media_caption
