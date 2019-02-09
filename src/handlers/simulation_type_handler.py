from Tkinter import *
from ttk import Combobox

import config
from src.handlers.base_handler import BaseHandler
from src.handlers.simulation_handler.flat_tensile_2d_test_handler import FlatTensile2DTestHandler


class SimulationTypeHandler(BaseHandler):
    """
    Simulation type and conditions handler
    """

    def __init__(self, frame):
        self.__simulation_types_map = {
            'Flat tensile test, 2D': FlatTensile2DTestHandler(),
        }
        super(SimulationTypeHandler, self).__init__(frame)

    def _configure(self):

        self.simulation_definition_frame = LabelFrame(self.frame, text='Simulation definition',
                                                      borderwidth=config.FRAME_BORDER_WIDTH,
                                                      relief=config.FRAME_RELIEF)
        self.simulation_definition_frame.grid(column=0, row=0, sticky=W + E + N, padx=config.FRAME_PADDING,
                                              pady=config.FRAME_PADDING)

        self.__simulation_type_label = Label(self.simulation_definition_frame, text='Simulation type')
        self.__simulation_type_label.grid(column=0, row=0, sticky=W, padx=config.FRAME_PADDING,
                                          pady=config.FRAME_PADDING)
        self.__simulation_type_variable = StringVar(value=self.__simulation_types_map.keys()[0])
        self.__simulation_type_combobox = Combobox(self.simulation_definition_frame,
                                                   values=self.__simulation_types_map.keys(),
                                                   textvariable=self.__simulation_type_variable)
        self.__simulation_type_combobox.grid(column=1, row=0, sticky=W, padx=config.FRAME_PADDING,
                                             pady=config.FRAME_PADDING)
        self.__simulation_type_combobox.bind('<<ComboboxSelected>>', self.__on_simulation_type_selected)

        self.__model_name_label = Label(self.simulation_definition_frame, text='Abaqus model name')
        self.__model_name_label.grid(column=2, row=0, sticky=E, padx=config.FRAME_PADDING,
                                     pady=config.FRAME_PADDING)
        self.model_name_variable = StringVar()
        self.__model_name_entry = Entry(self.simulation_definition_frame, textvariable=self.model_name_variable)
        self.__model_name_entry.grid(column=3, row=0, sticky=E, padx=config.FRAME_PADDING,
                                     pady=config.FRAME_PADDING)

        self.simulation_settings_frame = Frame(self.frame)
        self.simulation_settings_frame.grid(column=0, row=1, sticky=W + E + N + S)

        self.__on_simulation_type_selected(None)

    def __on_simulation_type_selected(self, _):
        choice = self.__simulation_type_variable.get()
        self.__simulation_types_map[choice].populate(self.simulation_settings_frame)
