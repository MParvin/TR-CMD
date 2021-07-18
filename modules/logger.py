#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging

### Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)

logger = logging.getLogger(__name__)
