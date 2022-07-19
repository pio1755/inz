$(document).ready(() => {
    const calendarDiv = $('#calendar');
    const userPanel = $('#user-panel');
    const schedule = $('#schedule');
    const hourLine = $('#hourLine');
    const reservationUrl = schedule.attr('data-finish-reservation-url');
    const workStartsAt = userPanel.attr('data-work-starts-at');
    const workEndsAt = userPanel.attr('data-work-ends-at');
    const workStartHour = new Date("1/1/1990 " + workStartsAt).getHours();
    const workEndHour = new Date("1/1/1990 " + workEndsAt).getHours();
    const scheduleRecordHeight = 150;
    let url;
    let interval;

    const currentHourLine = () => {
        const calendarTimeline = $('.calendar-timeline ul li');
        const dt = new Date();
        let currentHour = dt.getHours() + ":" + dt.getMinutes();
        currentHour = new Date("1/1/1990 " + currentHour);
        let startingHour = calendarTimeline.first().find('span').text();
        startingHour = new Date("1/1/1990 " + startingHour);
        let endingHour = calendarTimeline.last().find('span').text();
        endingHour = new Date("1/1/1990 " + endingHour);
        if (currentHour > startingHour && currentHour < endingHour) {
            const currentHourHeight = Math.round((currentHour.getTime() - startingHour.getTime()) / 60000);
            const heightPerMinute = scheduleRecordHeight / 60;
            return currentHourHeight * heightPerMinute;
        }
        return false;
    };

    const createTimeLIne = () => {
        const marginTop = currentHourLine() + 60;
        hourLine.empty();
        hourLine.append(`<div class='hour-line' style='margin-top: ${marginTop}; '></div>`);
    };

    const intervalTimeline = () => {
        if ($('.weektomonth').length || $('.daytoweek').length) {
            createTimeLIne();
            interval = setInterval(() => {
                createTimeLIne();
            }, 60 * 1000);
        } else {
            clearInterval(interval);
            hourLine.empty();
        }
    };

    const get_events = (eventsDate = false, worker = false) => {
        $.ajax({
            url: url,
            data: {
                eventsDate,
            },
            dataType: 'json',
            method: 'GET',
            success: data => {
                const {reservations, categories} = data;
                $.each(reservations, (entry, reservation) => {
                    calendar.addEvents({
                        start: reservation[0],
                        end: reservation[1],
                        title: reservation[4],
                        content: reservation[2],
                        category: reservation[3],
                    });
                });
                calendar.setEventCategoriesColors(
                    categories
                );
                calendar.reload();
                calendar.events = [];
                intervalTimeline();
                const columns = $('.calendar-events-day');
                $.each(columns, (entry, column) => {
                    const columnData = $(column).attr('data-time') * 1000;
                    const todayDate = new Date().setHours(0, 0, 0, 0);
                    if (todayDate > columnData) {
                        $(column).css('background-color', 'rgba(34,106,156,0.2)');
                    }
                });
            }
        });
    };

    const calendar = calendarDiv.Calendar({
        locale: 'pl',
        weekday: {
            timeline: {
                fromHour: workStartHour,
                toHour: workEndHour,
                heightPx: scheduleRecordHeight,
            }
        },
    });

    $('#schedule-panel #calendar').on('Calendar.init', (event, instance, before, current, after) => {
        url = $('#schedule-panel').attr('data-schedules-url');
        get_events(current);
    });
    $('#user-schedule-panel #calendar').on('Calendar.init', (event, instance, before, current, after) => {
        url = $('#user-schedule-panel').attr('data-schedules-url');
        get_events(current, true);
    });
    calendar.init();

    calendarDiv.on('click', '.calendar-event', target => {
        const reservationId = $(target.currentTarget).find('.event-name').text();
        $.ajax({
            url: reservationUrl,
            method: 'GET',
            data: {'id': reservationId},
            success: data => {
                $('.modal-content').html(data);
                if ($('#id_is_finished').val() === 'True') {
                    $('#submit').hide()
                }
                $('.modal').modal('show');
            }
        });
    });

    $('#scheduleModal').on('click', '#submit', event => {
        event.preventDefault();
        const finishForm = $('#finishReservationForm');
        finishForm.find('#id_is_finished').val(true);
        $.ajax({
            url: reservationUrl,
            method: 'POST',
            data: finishForm.serialize(),
            success: data => {
                $('.modal').modal('hide');
            }
        });
    });
    createTimeLIne()
});


