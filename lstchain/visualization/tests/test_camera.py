import numpy as np
from lstchain.visualization.camera import overlay_source, overlay_disp_vector, display_dl1_event
from lstchain.reco.disp import disp_parameters_event
from ctapipe.visualization import CameraDisplay
from ctapipe.instrument import CameraGeometry
import astropy.units as u

def test_overlay_disp_vector():

    from ctapipe.image import hillas_parameters

    geom = CameraGeometry.from_name('LSTCam')
    image = np.random.rand(geom.n_pixels)
    display = CameraDisplay(geom, image)
    hillas = hillas_parameters(geom, image)
    disp = disp_parameters_event(hillas, 0.1*u.m, 0.3*u.m)
    overlay_disp_vector(display, disp, hillas)


def test_overlay_source():
    geom = CameraGeometry.from_name('LSTCam')
    image = np.random.rand(geom.n_pixels)
    display = CameraDisplay(geom, image)
    overlay_source(display, 0.1, 0.3)


def test_display_dl1_event():
    from ctapipe.io import event_source, EventSeeker
    from lstchain.tests.test_lstchain import mc_gamma_testfile
    from ctapipe.calib import CameraCalibrator
    source = event_source(mc_gamma_testfile, back_seekable=True)
    seeker = EventSeeker(source)
    event = seeker[11]  # event 11 has telescopes 1 and 4 with data
    CameraCalibrator()(event)
    display_dl1_event(event, tel_id=1)
    display_dl1_event(event, tel_id=4)