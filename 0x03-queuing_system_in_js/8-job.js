/**
 * Create a queue of jobs to be
 * processed.
 *
 * @params {object} - An array of job
 * objects.
 * @params {object} - An instance of a
 * queue to help create jobs.
 *
 */
const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) throw new Error('Jobs is not an array');

  jobs.forEach((job) => {
    const jobCreated = queue.create('push_notification_code_3', job).save((err) => {
      if (!err) console.log(`Notification job created: ${jobCreated.id}`);
    });

    jobCreated.on('complete', () => { console.log(`Notification job ${jobCreated.id} completed`); });
    jobCreated.on('failed', (err) => { console.log(`Notification job ${jobCreated.id} failed: ${err}`); });
    jobCreated.on('progress', (progress) => { console.log(`Notification job ${jobCreated.id} ${progress}% complete`); });
  });
};

export default createPushNotificationsJobs;
