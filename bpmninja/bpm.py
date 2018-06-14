# Import flask dependencies
from flask_restplus import Resource, Namespace, reqparse

bpm_ns = Namespace("bpm", description="GET bpm data by song ID")

# Expected arguments for bpm /GET request
bpm_parser = reqparse.RequestParser()
bpm_parser.add_argument('songId', type=int, help='Song ID: type=int')


@bpm_ns.route("/")
class BPM(Resource):
    """
    /bpm: Returns ALL data for ALL songs.

    OPTIONAL PARAMS:
    * /<songId>: returns all data for a single song.

    """
    @bpm_ns.expect(bpm_parser, validate=True)
    def get(self):
        """Get all bpm data."""

        args = bpm_parser.parse_args()

        if args['songId']:
            single_song = {
                123: {
                    "bpm": 155,
                    "songTitle": "A Smooth One",
                    "artist": "Charlie Christian",
                    "album": "Best of Charlie Christian",
                    "artwork": "format tbd"
                }
            }

            return single_song, 200
        else:
            multi_song = [
                {
                    12: {
                        "bpm": 155,
                        "songTitle": "A Smooth One",
                        "artist": "Charlie Christian",
                        "album": "Best of Charlie Christian",
                        "artwork": "format tbd"
                    }
                },
                {
                    13: {
                        "bpm": 199,
                        "songTitle": "Flying Home",
                        "artist": "Lionel Hampton",
                        "album": "Lionel's Hits",
                        "artwork": "format tbd"
                    }
                }

            ]

            return multi_song, 200
