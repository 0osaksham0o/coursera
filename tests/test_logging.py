import logging

def test_logging_setup():
    logger = logging.getLogger("ai_workflow")
    assert logger is not None
