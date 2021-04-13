import plotly.graph_objects as go

def create_candlestick_chart(result_df,conversion_from,conversion_to):
	fig = go.Figure(data=[go.Candlestick(x=result_df['time_period_start'],
                open=result_df['price_open'],
                high=result_df['price_high'],
                low=result_df['price_low'],
                close=result_df['price_close'])])

	fig.update_layout(
	title=conversion_from + " to " + conversion_to,
	yaxis_title='Conversion Rate',xaxis_title = 'Time'
	)
	return fig