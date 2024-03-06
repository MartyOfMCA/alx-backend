const kue = require('kue');

const queue = kue.createQueue();
const sendNotification = (phoneNumber, message, jobId, done) => {
  console.log(`Job ${jobId}: Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
};

queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job.id, done);
});
