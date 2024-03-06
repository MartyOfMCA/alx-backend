/**
 * Define a job processor to send notifications
 * to a list of phone numbers.
 *
 */
const kue = require('kue');

const blacklist = ['4153518780', '4153518781'];
const queue = kue.createQueue();

/**
 * Send the given notification message
 * to the given phone number.
 *
 * @params {string} - The receiving phone
 * number.
 * @params {string} - The message to send.
 * @params {object} - The Job instance containing
 * details of the job to be processed.
 * @params {function) - The callback to
 * idicate the status of the operation.
 *
 */
const sendNotification = (phoneNumber, message, job, done) => {
  // Set job progress to 0 out of 100.
  job.progress(0, 100);
  // Check for blacklisted numbers and
  // abort the operation.
  if (blacklist.includes(phoneNumber)) return (done(new Error(`Phone number ${phoneNumber} is blacklisted`)));

  // Assume job is halfway done.
  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
};

// Process jobs named push_notification_code_2
// in the queue.
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;

  // Invoke process handler to send notification.
  sendNotification(phoneNumber, message, job, done);
});
