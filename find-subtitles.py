#!/usr/bin/env python3

from datetime import timedelta

from babelfish import Language
from subliminal import download_best_subtitles, region, save_subtitles, scan_videos
from subliminal.core import search_external_subtitles

from libs.personalConfig import config
from libs.personalLogger import logger

if not config['LEGENDASTV']['username']:
    logger.info("Problem in configuration")

if not config['LEGENDASTV']['password']:
    logger.info("Problem in configuration")

if not config['OPENSUBTITLE']['username']:
    logger.info("Problem in configuration")

if not config['OPENSUBTITLE']['password']:
    logger.info("Problem in configuration")

if not config['ADDIC7ED']['username']:
    logger.info("Problem in configuration")

if not config['ADDIC7ED']['password']:
    logger.info("Problem in configuration")

if not config['MEDIA']['path']:
    logger.info("Problem in configuration")

providers = {
    'opensubtitles': True,
    'legendastv': True,
    'addic7ed': True,
}

provider_settings = {
    'opensubtitles': {
        'username': config['OPENSUBTITLE']['username'],
        'password': config['OPENSUBTITLE']['password']
    },
    'legendastv': {
        'username': config['LEGENDASTV']['username'],
        'password': config['LEGENDASTV']['password']
    },
    'addic7ed': {
        'username': config['ADDIC7ED']['username'],
        'password': config['ADDIC7ED']['password']
    },
}

region.configure('dogpile.cache.memory')

pathMedias = config['MEDIA']['path']

medias = []
for video in scan_videos(pathMedias, age=timedelta(weeks=4)):
    # Checking if the vidos has subltitles and what languages is it
    video.subtitle_languages |= set(search_external_subtitles(video.name).values())
    medias.append(video)

possibleSubtitles = download_best_subtitles(medias, {Language('eng'), Language('por', 'BR')},
                                            providers=providers, provider_configs=provider_settings)
for video in medias:
    logger.info("Searching subtitles for %s", video.name)
    if possibleSubtitles[video]:
        logger.info("Downdload subtitles for %s", video.name)
        for videoSubtitle in possibleSubtitles[video]:
            logger.info("   - Language %s", videoSubtitle.language.alpha3)
        save_subtitles(video, possibleSubtitles[video])
