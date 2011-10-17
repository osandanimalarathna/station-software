
export_values = {
    'CIC': [
        ('N', 'RED', 'data_reduction'),
        ('N', 'EVENTRATE', 'eventrate'),
        ('N', 'TRIGPATTERN', 'trigger_pattern'),
        ('Y', 'STDDEV1', 'mas_stdev1'),
        ('Y', 'STDDEV2', 'mas_stdev2'),
        ('Y', 'STDDEV3', 'slv_stdev1'),
        ('Y', 'STDDEV4', 'slv_stdev2'),
        ('Y', 'BL1', 'mas_baseline1'),
        ('Y', 'BL2', 'mas_baseline2'),
        ('Y', 'BL3', 'slv_baseline1'),
        ('Y', 'BL4', 'slv_baseline2'),
        ('Y', 'NP1', 'mas_npeaks1'),
        ('Y', 'NP2', 'mas_npeaks2'),
        ('Y', 'NP3', 'slv_npeaks1'),
        ('Y', 'NP4', 'slv_npeaks2'),
        ('Y', 'PH1', 'mas_pulseheight1'),
        ('Y', 'PH2', 'mas_pulseheight2'),
        ('Y', 'PH3', 'slv_pulseheight1'),
        ('Y', 'PH4', 'slv_pulseheight2'),
        ('Y', 'IN1', 'mas_int1'),
        ('Y', 'IN2', 'mas_int2'),
        ('Y', 'IN3', 'slv_int1'),
        ('Y', 'IN4', 'slv_int2'),
        ('N', 'TR1', 'mas_tr1'),
        ('N', 'TR2', 'mas_tr2'),
        ('N', 'TR3', 'slv_tr1'),
        ('N', 'TR4', 'slv_tr2')],
    'ERR': [('N', 'ERRMSG', 'error_message')],
    'CFG': [
        ('N', 'CFG_GPS_LAT', 'cfg_gps_latitude'),
        ('N', 'CFG_GPS_LONG', 'cfg_gps_longitude'),
        ('N', 'CFG_GPS_ALT', 'cfg_gps_altitude'),
        ('N', 'CFG_MAS_VERSION', 'cfg_mas_version'),
        ('N', 'CFG_SLV_VERSION', 'cfg_slv_version'),
        ('N', 'CFG_TRIGLOWSIG', 'cfg_trig_low_signals'),
        ('N', 'CFG_TRIGHIGHSIG', 'cfg_trig_high_signals'),
        ('N', 'CFG_TRIGEXT', 'cfg_trig_external'),
        ('N', 'CFG_TRIGANDOR', 'cfg_trig_and_or'),
        ('N', 'CFG_PRECTIME', 'cfg_precoinctime'),
        ('N', 'CFG_CTIME', 'cfg_coinctime'),
        ('N', 'CFG_POSTCTIME', 'cfg_postcoinctime'),
        ('N', 'CFG_DETNUM', 'cfg_detnum'),
        ('N', 'CFG_PASSWORD', 'cfg_password'),
        ('N', 'CFG_SPAREBYTES', 'cfg_spare_bytes'),
        ('N', 'CFG_USEFILTER', 'cfg_use_filter'),
        ('N', 'CFG_USEFILTTHRES', 'cfg_use_filter_threshold'),
        ('N', 'CFG_REDUCE', 'cfg_reduce_data'),
        ('N', 'CFG_BUFFER', 'cfg_buffer'),
        ('N', 'CFG_STARTMODE', 'cfg_startmode'),
        ('N', 'CFG_DELAYSCREEN', 'cfg_delay_screen'),
        ('N', 'CFG_DELAYCHECK', 'cfg_delay_check'),
        ('N', 'CFG_DELAYERROR', 'cfg_delay_error'),
        ('N', 'CFG_MAS_CH1THRLOW', 'cfg_mas_ch1_thres_low'),
        ('N', 'CFG_MAS_CH1THRHIGH', 'cfg_mas_ch1_thres_high'),
        ('N', 'CFG_MAS_CH2THRLOW', 'cfg_mas_ch2_thres_low'),
        ('N', 'CFG_MAS_CH2THRHIGH', 'cfg_mas_ch2_thres_high'),
        ('N', 'CFG_MAS_CH1INTTIME', 'cfg_mas_ch1_inttime'),
        ('N', 'CFG_MAS_CH2INTTIME', 'cfg_mas_ch2_inttime'),
        ('N', 'CFG_MAS_CH1VOLT', 'cfg_mas_ch1_voltage'),
        ('N', 'CFG_MAS_CH2VOLT', 'cfg_mas_ch2_voltage'),
        ('N', 'CFG_MAS_CH1CURR', 'cfg_mas_ch1_current'),
        ('N', 'CFG_MAS_CH2CURR', 'cfg_mas_ch2_current'),
        ('N', 'CFG_MAS_COMPTHRLOW', 'cfg_mas_comp_thres_low'),
        ('N', 'CFG_MAS_COMPTHRHIGH', 'cfg_mas_comp_thres_high'),
        ('N', 'CFG_MAS_MAXVOLT', 'cfg_mas_max_voltage'),
        ('N', 'CFG_MAS_RESET', 'cfg_mas_reset'),
        ('N', 'CFG_MAS_CH1GAINPOS', 'cfg_mas_ch1_gain_pos'),
        ('N', 'CFG_MAS_CH1GAINNEG', 'cfg_mas_ch1_gain_neg'),
        ('N', 'CFG_MAS_CH2GAINPOS', 'cfg_mas_ch2_gain_pos'),
        ('N', 'CFG_MAS_CH2GAINNEG', 'cfg_mas_ch2_gain_neg'),
        ('N', 'CFG_MAS_CH1OFFPOS', 'cfg_mas_ch1_offset_pos'),
        ('N', 'CFG_MAS_CH1OFFNEG', 'cfg_mas_ch1_offset_neg'),
        ('N', 'CFG_MAS_CH2OFFPOS', 'cfg_mas_ch2_offset_pos'),
        ('N', 'CFG_MAS_CH2OFFNEG', 'cfg_mas_ch2_offset_neg'),
        ('N', 'CFG_MAS_COMMOFF', 'cfg_mas_common_offset'),
        ('N', 'CFG_MAS_INTVOLTAGE', 'cfg_mas_internal_voltage'),
        ('N', 'CFG_MAS_CH1ADCGAIN', 'cfg_mas_ch1_adc_gain'),
        ('N', 'CFG_MAS_CH1ADCOFF', 'cfg_mas_ch1_adc_offset'),
        ('N', 'CFG_MAS_CH2ADCGAIN', 'cfg_mas_ch2_adc_gain'),
        ('N', 'CFG_MAS_CH2ADCOFF', 'cfg_mas_ch2_adc_offset'),
        ('N', 'CFG_MAS_CH1COMPGAIN', 'cfg_mas_ch1_comp_gain'),
        ('N', 'CFG_MAS_CH1COMPOFF', 'cfg_mas_ch1_comp_offset'),
        ('N', 'CFG_MAS_CH2COMPGAIN', 'cfg_mas_ch2_comp_gain'),
        ('N', 'CFG_MAS_CH2COMPOFF', 'cfg_mas_ch2_comp_offset'),
        ('N', 'CFG_SLV_CH1THRLOW', 'cfg_slv_ch1_thres_low'),
        ('N', 'CFG_SLV_CH1THRHIGH', 'cfg_slv_ch1_thres_high'),
        ('N', 'CFG_SLV_CH2THRLOW', 'cfg_slv_ch2_thres_low'),
        ('N', 'CFG_SLV_CH2THRHIGH', 'cfg_slv_ch2_thres_high'),
        ('N', 'CFG_SLV_CH1INTTIME', 'cfg_slv_ch1_inttime'),
        ('N', 'CFG_SLV_CH2INTTIME', 'cfg_slv_ch2_inttime'),
        ('N', 'CFG_SLV_CH1VOLT', 'cfg_slv_ch1_voltage'),
        ('N', 'CFG_SLV_CH2VOLT', 'cfg_slv_ch2_voltage'),
        ('N', 'CFG_SLV_CH1CURR', 'cfg_slv_ch1_current'),
        ('N', 'CFG_SLV_CH2CURR', 'cfg_slv_ch2_current'),
        ('N', 'CFG_SLV_COMPTHRLOW', 'cfg_slv_comp_thres_low'),
        ('N', 'CFG_SLV_COMPTHRHIGH', 'cfg_slv_comp_thres_high'),
        ('N', 'CFG_SLV_MAXVOLT', 'cfg_slv_max_voltage'),
        ('N', 'CFG_SLV_RESET', 'cfg_slv_reset'),
        ('N', 'CFG_SLV_CH1GAINPOS', 'cfg_slv_ch1_gain_pos'),
        ('N', 'CFG_SLV_CH1GAINNEG', 'cfg_slv_ch1_gain_neg'),
        ('N', 'CFG_SLV_CH2GAINPOS', 'cfg_slv_ch2_gain_pos'),
        ('N', 'CFG_SLV_CH2GAINNEG', 'cfg_slv_ch2_gain_neg'),
        ('N', 'CFG_SLV_CH1OFFPOS', 'cfg_slv_ch1_offset_pos'),
        ('N', 'CFG_SLV_CH1OFFNEG', 'cfg_slv_ch1_offset_neg'),
        ('N', 'CFG_SLV_CH2OFFPOS', 'cfg_slv_ch2_offset_pos'),
        ('N', 'CFG_SLV_CH2OFFNEG', 'cfg_slv_ch2_offset_neg'),
        ('N', 'CFG_SLV_COMMOFF', 'cfg_slv_common_offset'),
        ('N', 'CFG_SLV_INTVOLTAGE', 'cfg_slv_internal_voltage'),
        ('N', 'CFG_SLV_CH1ADCGAIN', 'cfg_slv_ch1_adc_gain'),
        ('N', 'CFG_SLV_CH1ADCOFF', 'cfg_slv_ch1_adc_offset'),
        ('N', 'CFG_SLV_CH2ADCGAIN', 'cfg_slv_ch2_adc_gain'),
        ('N', 'CFG_SLV_CH2ADCOFF', 'cfg_slv_ch2_adc_offset'),
        ('N', 'CFG_SLV_CH1COMPGAIN', 'cfg_slv_ch1_comp_gain'),
        ('N', 'CFG_SLV_CH1COMPOFF', 'cfg_slv_ch1_comp_offset'),
        ('N', 'CFG_SLV_CH2COMPGAIN', 'cfg_slv_ch2_comp_gain'),
        ('N', 'CFG_SLV_CH2COMPOFF', 'cfg_slv_ch2_comp_offset')],
    'CMP': [
        ('N', 'CMP_DEVICE', 'cmp_device'),
        ('N', 'CMP_COMPARATOR', 'cmp_comparator'),
        ('N', 'CMP_COUNT', 'cmp_count_over_threshold')],
    'WTR': [
        ('N', 'WTR_TEMP_INSIDE', 'tempInside'),
        ('N', 'WTR_TEMP_OUTSIDE', 'tempOutside'),
        ('N', 'WTR_HUMIDITY_OUTSIDE', 'humidityOutside'),
        ('N', 'WTR_HUMIDITY_INSIDE', 'humidityInside'),
        ('N', 'WTR_BAROMETER', 'barometer'),
        ('N', 'WTR_WIND_DIR', 'windDir'),
        ('N', 'WTR_WIND_SPEED', 'windSpeed'),
        ('N', 'WTR_SOLAR_RAD', 'solarRad'),
        ('N', 'WTR_UV', 'UV'),
        ('Y', 'WTR_ET', 'ET'),
        ('N', 'WTR_RAIN_RATE', 'rainRate'),
        ('Y', 'WTR_HEAT_INDEX', 'heatIndex'),
        ('Y', 'WTR_DEW_POINT', 'dewPoint'),
        ('Y', 'WTR_WIND_CHILL', 'windChill')],
}
