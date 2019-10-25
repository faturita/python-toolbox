% generate some fake data
t = 0:60;
trend = 0.003*t.^2;
x = trend + sin(0.1*2*pi*t) + randn(1,numel(t))*0.5;

% estimate trend using polyfit
p_est = polyfit(t,x,3);
trend_est = polyval(p_est,t);

% plot results
plot(t,x,t,trend,t,trend_est,t,x-trend_est);
legend('data','trend','estimated trend','trend removed','Location','NorthWest');
