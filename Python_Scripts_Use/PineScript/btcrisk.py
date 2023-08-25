//@version=5
indicator("Improved Bitcoin Risk Indicator", shorttitle="BTC Risk", overlay=false)

len1 = input.int(50, minval=1, title="Short-term SMA Length (Default: 50)")
len2 = input.int(350, minval=1, title="Long-term SMA Length (Default: 350)")
threshold = input.float(0.75, minval=0.01, maxval=1, step=0.01, title="Risk Threshold (Default: 0.75)")

showThreshold = input.bool(true, title="Show Risk Threshold Line")

dailyClose = request.security(syminfo.tickerid, "D", close)
src1 = ta.sma(dailyClose, len1)
src2 = ta.sma(dailyClose, len2)

SMARatio = (src1 / src2)
lookback = input.int(4000, minval=1, title="Lookback Period")
SMARatioMaxVal = ta.highest(SMARatio, lookback)

SMARatioNormalized = SMARatio / SMARatioMaxVal

// Color coding for risk levels
lowRiskColor = color.new(color.green, 80)
mediumRiskColor = color.new(color.yellow, 80)
highRiskColor = color.new(color.red, 80)

lineColor = SMARatioNormalized < 0.5 ? lowRiskColor : SMARatioNormalized < threshold ? mediumRiskColor : highRiskColor

// Plot normalized SMA ratio with color coding
plot(SMARatioNormalized, color=lineColor, linewidth=2, title="Normalized SMA Ratio")


// Display the current risk level as a label
var label riskLabel = label.new(x=bar_index, y=SMARatioNormalized, style=label.style_label_down, color=color(na))
label.set_xy(riskLabel, bar_index, SMARatioNormalized)
label.set_text(riskLabel, "Risk: " + str.tostring(SMARatioNormalized * 100, "%.2f") + "%")
label.set_color(riskLabel, color = color.white)
label.set_style(riskLabel, SMARatioNormalized < 0.5 ? label.style_label_down : label.style_label_up
