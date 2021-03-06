"""API routing for /GET endpoints, to get BPM data by song ID."""
from bpmninja.song_metadata import song_metadata
from flask_restplus import Resource, Namespace, reqparse

bpm_ns = Namespace("bpm", description="GET bpm data by song ID")

# Expected arguments for bpm /GET request
bpm_parser = reqparse.RequestParser()
bpm_parser.add_argument('songId', type=int, help='Int between 0 and {}'.format(len(song_metadata) - 1))


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

        if args['songId'] is not None:
            try:
                result = song_metadata[args['songId']]
                return result, 200
            except KeyError as err:
                return 'songId {} is invalid. Must be between 0 and {}'.format(err, len(song_metadata) - 1), 404
        return song_metadata
