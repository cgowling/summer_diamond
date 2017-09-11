        in_pData[0].plugin_data_setup(pattern, self.get_max_frames())
        out_pData[0].plugin_data_setup(
                pattern, in_pData[0]._get_max_frames_process())

    def get_max_frames(self):
        return 'multiple'