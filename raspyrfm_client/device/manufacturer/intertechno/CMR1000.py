from raspyrfm_client.device import actions
from raspyrfm_client.device.manufacturer.universal.HX2262Compatible import HX2262Compatible


class CMR1000(HX2262Compatible):
    _argchecks = {
        'master': '^[A-P]$',
		'slave': '^([1-9]|[0][1-9]|[1][1-6])$'
    }
    
    _l = '0'
    _h = 'f'
    _on = [_h, _h]
    _off = [_h, _l]

    def __init__(self):
        from raspyrfm_client.device.manufacturer import manufacturer_constants
        super().__init__(manufacturer_constants.INTERTECHNO, manufacturer_constants.CMR_1000)

    def get_supported_actions(self) -> [str]:
        return [actions.ON, actions.OFF]
        
    def get_bits(self, action: str):
        cfg = self.get_channel_config()
        bits = []
        
        master = ord(cfg['master']) - ord('A')
        bits += self.calc_int_bits(master, 4)
        
        slave = int(cfg['slave']) - 1
        bits += self.calc_int_bits(slave, 4)
        
        bits += ['0', 'f'] #fixed
        
        if action is actions.ON:
            bits += self._on
        elif action is actions.OFF:
            bits += self._off
            
        return bits