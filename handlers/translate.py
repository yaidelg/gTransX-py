'''<HANDLER DESCRIPTION>'''

import json
import logging
import os
from deep_translator import GoogleTranslator

log_level = os.environ.get('LOG_LEVEL', 'INFO')
logging.root.setLevel(logging.getLevelName(log_level))  # type: ignore
_logger = logging.getLogger(__name__)


def handler(event, context):
    '''Function entry'''
    _logger.debug('Event: {}'.format(json.dumps(event)))
    data = event['body']
    src = data["src"]
    tgt = data["tgt"]
    service = data["service"]
    texts = data["texts"]
    translated = []
    try:
        translated = GoogleTranslator(src, tgt).translate_batch(texts)
    except Exception as e:
        _logger.error('failed: {}'.format(e), exc_info=True)

    return {
        'statusCode': 200,
        'headers': {"Content-Type": "text/plain"},
        'body': json.dumps({
            'rc': 0,
            'msg': "Success!",
            'texts': translated,
        })
    }
