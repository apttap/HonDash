import os
import subprocess
from shutil import copyfile
from unittest import mock

from backend.backend import Backend
from devices import setup_file

from devices.setup_file import SetupFile

from backend import backend


class TestBackend:
    def setup_method(self):
        # prepare the setup file where the backend expects it
        copyfile(setup_file.DEFAULT_CONFIG_FILE_NAME, setup_file.FILE_NAME)
        subprocess.Popen(["venv/bin/crossbar", "start"])  # start websocket

    def teardown_method(self):
        os.remove("setup.json")  # delete setup file
        subprocess.Popen(["venv/bin/crossbar", "stop"])  # close websocket

    def test_get_backend(self):
        """
        calling the getter method of the class should return a Backend instance
        """
        with mock.patch("devices.kpro.kpro.Kpro.__init__") as m___init__:
            m___init__.return_value = (
                None  # mocking kpro device since for tests is not available
            )
            backend = Backend.get()

        assert type(backend) == Backend

    def test_rpc_setup(self):
        """
        remote procedure call setup() should return the json setup loaded.
        """
        setup_file = SetupFile()

        with mock.patch("devices.setup_file.SetupFile.load_setup") as m_load_setup:
            json = backend.setup()
            assert m_load_setup.called is True
            assert setup_file.load_setup() == json

    def test_rpc_reset(self):
        """
        """

        with mock.patch("devices.setup_file.SetupFile.reset_setup") as m_reset_setup,\
                mock.patch("autobahn_sync.publish", side_effect=None) as m_publish:
            m_publish.return_value=None
            backend.reset()
            assert m_reset_setup.called is True
            assert m_publish.assert_called_with(None)
