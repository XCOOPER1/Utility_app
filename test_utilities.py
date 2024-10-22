import pytest
import shutil
import psutil
from Utility_app import check_disk_usage, check_cpu_usage

# Mock the responses for disk and CPU usage
@pytest.fixture
def mock_disk_usage(monkeypatch):
    def mock_usage(disk):
        class DiskUsage:
            total = 100
            free = 30  # 30% free space
        return DiskUsage()
    monkeypatch.setattr(shutil, 'disk_usage', mock_usage)

@pytest.fixture
def mock_cpu_usage(monkeypatch):
    def mock_usage(interval):
        return 50  # 50% CPU usage
    monkeypatch.setattr(psutil, 'cpu_percent', mock_usage)

# Test cases
def test_check_disk_usage(mock_disk_usage):
    assert check_disk_usage("C:/") == True

def test_check_cpu_usage(mock_cpu_usage):
    assert check_cpu_usage() == True
