# PowerSupplyRemoteControl
Remote control of PSU via serial terminal connection through Python.

## Supported devices
1. [Velleman LABPS3005DN](#velleman-labps30005dn)

### Velleman LABPS30005DN
| Function | Usage | Returns |
|---|---|---|
| getID | Get PSU ID | String |
| getCurrent | Get current limit | Float |
| getVoltage | Get voltage setpoint | Float |
| getRealCurrent | Get actual output current | Float (2.2) |
| getRealVoltage | Get actual voltage output | Float (1.3) |
| getStatus | Get status flags | String |
| getFlagCV | Check Constant Voltage glag | Boolean |
| getFlagOutput | Check output active flag | Boolean |
| getFlagOCP | Check Over Current Protection flag | Boolean |
| setCurrent | Set new current limit | N/A |
| setVoltage | Set new voltage setpoint | N/A |
| setOutput | Set output state | N/A |